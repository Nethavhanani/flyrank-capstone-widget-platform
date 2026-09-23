from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.limiter import limiter
from app.models.models import Widget, Submission
from app.schemas.submission import SubmissionCreate, SubmissionResponse

router = APIRouter()

@router.post("/", response_model=SubmissionResponse, status_code=status.HTTP_201_CREATED)
@limiter.limit("10/minute")
def create_submission(
    request: Request,
    submission_in: SubmissionCreate,
    db: Session = Depends(get_db)
):
    # 1. Verify target widget exists
    widget = db.query(Widget).filter(Widget.id == submission_in.widget_id).first()
    if not widget:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Widget with ID '{submission_in.widget_id}' not found."
        )

    # 2. Extract client IP address (handles reverse proxies)
    client_ip = request.headers.get("x-forwarded-for")
    if client_ip:
        client_ip = client_ip.split(",")[0].strip()
    else:
        client_ip = request.client.host if request.client else None

    # 3. Create and persist submission
    db_submission = Submission(
        widget_id=submission_in.widget_id,
        payload=submission_in.payload,
        ip_address=client_ip,
        geo_data=None  # Can be populated via GeoIP middleware/service later
    )
    
    db.add(db_submission)
    db.commit()
    db.refresh(db_submission)

    return db_submission
