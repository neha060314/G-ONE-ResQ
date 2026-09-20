from fastapi import APIRouter
from src.patient.provider import MockPatientProvider
from src.protocols.registry import ProtocolRegistry

router = APIRouter(prefix="/api/v1")
patient_provider = MockPatientProvider()
protocol_registry = ProtocolRegistry()

@router.get("/patients")
async def list_patients():
    return [p.model_dump() for p in patient_provider._database.values()]

@router.get("/protocols")
async def list_protocols():
    return {k: v.model_dump() for k, v in protocol_registry._protocols.items()}

@router.get("/health")
async def health_check():
    return {"status": "ok", "service": "G-ONE ResQ"}