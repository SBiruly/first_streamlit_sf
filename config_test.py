import streamlit as st

# Define the Streamlit app
st.title("Configuration Input")

# Create input fields for SQL Server connection
st.header("SQL Server Connection")
sql_host = st.text_input("Host", "192.168.0.231")
sql_src_db = st.text_input("Source Database", "TestDB")
sql_user = st.text_input("User", "sa")
sql_password = st.text_input("Password", type="password")
sql_port = st.number_input("Port", 1433)

# Create input fields for Snowflake connection
st.header("Snowflake Connection")
sf_url = st.text_input("Snowflake URL", "https://fpb94648.us-east-1.snowflakecomputing.com")
sf_warehouse = st.text_input("Snowflake Warehouse", "COMPUTE_WH")
sf_database = st.text_input("Snowflake Database", "SF_DEV")
sf_schema = st.text_input("Snowflake Schema", "SF_MARKETING_DEV")
sf_user = st.text_input("Snowflake User", "OPTIMIZATION")
sf_password = st.text_input("Snowflake Password", type="password")
sf_role = st.text_input("Snowflake Role", "ACCOUNTADMIN")
sf_region = st.text_input("Snowflake Region", "AWS_US_EAST_1")
external_stage_name = st.text_input("External Stage Name", "AWS_DM_EXT_STG")
source_schema = st.text_input("Source Schema", "SF_MARKETING_DEV")
target_schema = st.text_input("Target Schema", "dm_tgt_schema")
snowflake_account = st.text_input("Snowflake Account", "fpb94648.us-east-1")
log_table_name = st.text_input("Log Table Name", "log_table")

# Save the configuration to a text file
if st.button("Save Configuration"):
    with open("config.txt", "w") as file:
        file.write("[SQL_SERVER_CONNECTION]\n")
        file.write(f"host = {sql_host}\n")
        file.write(f"src_db = {sql_src_db}\n")
        file.write(f"user = {sql_user}\n")
        file.write(f"password = {sql_password}\n")
        file.write(f"port = {sql_port}\n\n")

        file.write("[TARGET_SNOWFLAKE]\n")
        file.write(f"sfURL = {sf_url}\n")
        file.write(f"sfWarehouse = {sf_warehouse}\n")
        file.write(f"sfDatabase = {sf_database}\n")
        file.write(f"sfSchema = {sf_schema}\n")
        file.write(f"sfUser = {sf_user}\n")
        file.write(f"sfPassword = {sf_password}\n")
        file.write(f"sfRole = {sf_role}\n")
        file.write(f"sfRegion = {sf_region}\n")
        file.write(f"external_stage_name = {external_stage_name}\n")
        file.write(f"source_schema = {source_schema}\n")
        file.write(f"target_schema = {target_schema}\n")
        file.write(f"snowflake_account = {snowflake_account}\n")
        file.write(f"log_table_name = {log_table_name}\n")

    st.success("Configuration saved to config.txt")

# Run the Streamlit app
if __name__ == "__main__":
    st.set_option('deprecation.showfileUploaderEncoding', False)
    st.set_page_config(layout="wide")
    st.write("To save the configuration, fill in the fields above and click 'Save Configuration'.")
