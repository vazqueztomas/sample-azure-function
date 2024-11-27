import azure.functions as func
from sample_azure_function.sample_function import bp
from sample_azure_function.sample_function.orchestrator import df_bp as orchestrator_bp


app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

# Register the blueprint (sample_function)
app.register_functions(bp)
app.register_functions(orchestrator_bp)
