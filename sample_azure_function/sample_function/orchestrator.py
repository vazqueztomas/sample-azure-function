import azure.functions as func
import azure.durable_functions as df
from .trigger import bp

app = df.DFApp(http_auth_level=func.AuthLevel.ANONYMOUS)


@bp.orchestration_trigger(context_name="context")
def orchestrator_function(context: df.DurableOrchestrationContext):
    # This will start the activity function
    result = yield context.call_activity("sample_activity", "Azure")
    return result

main = df.Orchestrator.create(orchestrator_function)