from lambda_freezer import run_after_default_deployment, deploy

if __name__ == "__main__":
    APILIB_REST_API_ID = "r5ltm5nqr7"
    APILIB_REGION = "us-east-1"
    APILIB_DOMAIN_NAME = "api-library.bambu.life"

    run_after_default_deployment(REST_API_ID, REGION, DOMAIN_NAME)
    deploy(REST_API_ID, REGION, "1.2.0", "some description!", DOMAIN_NAME)
