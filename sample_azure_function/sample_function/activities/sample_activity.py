from sample_function.orchestrator import df_bp
import logging


@df_bp.activity_trigger(input_name="city")
def say_hello(city: str) -> str:
    logging.info(f"Saying hello to {city}")
    return f"Hello {city}!"
