import logging
import azure.functions as func
import azure.durable_functions as df

df_bp = df.Blueprint()


@df_bp.route(route="startOrchestrator")
@df_bp.durable_client_input(client_name="client")
async def start_orchestrator(req: func.HttpRequest, client):
    instance_id = await client.start_new("my_orchestrator")

    logging.info(f"Started orchestration with ID = '{instance_id}'.")
    return client.create_check_status_response(req, instance_id)


@df_bp.orchestration_trigger(context_name="context")
def my_orchestrator(context: df.DurableOrchestrationContext):
    result1 = yield context.call_activity("say_hello", "Tokyo")
    result2 = yield context.call_activity("say_hello", "Seattle")
    result3 = yield context.call_activity("say_hello", "London")
    return [result1, result2, result3]

