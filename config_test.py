import streamlit as st

# Define the Streamlit app
st.title("Configuration Input")

# Create input fields for SQL Server connection
st.header("SQL Server Connection")
sql_host = st.text_input("Host",  help="Enter the SQL Server host")
sql_src_db = st.text_input("Source Database",  help="Enter the source database name")
sql_user = st.text_input("User",  help="Enter the SQL Server user")
sql_password = st.text_input("Password", type="password", help="Enter the SQL Server password")
sql_port = st.number_input("Port",value = 1433,help="Enter the SQL Server port")

# Create input fields for Snowflake connection
st.header("Snowflake Connection")
sf_url = st.text_input("Snowflake URL", help="Enter the Snowflake URL")
sf_warehouse = st.text_input("Snowflake Warehouse", help="Enter the Snowflake Warehouse")
sf_database = st.text_input("Snowflake Database",  help="Enter the Snowflake Database")
sf_schema = st.text_input("Snowflake Schema",  help="Enter the Snowflake Schema")
sf_user = st.text_input("Snowflake User", help="Enter the Snowflake User")
sf_password = st.text_input("Snowflake Password", type="password", help="Enter the Snowflake password")
sf_role = st.text_input("Snowflake Role",  help="Enter the Snowflake Role")
sf_region = st.text_input("Snowflake Region",  help="Enter the Snowflake Region")
external_stage_name = st.text_input("External Stage Name",  help="Enter the External Stage Name")
source_schema = st.text_input("Source Schema",  help="Enter the Source Schema")
target_schema = st.text_input("Target Schema",  help="Enter the Target Schema")
snowflake_account = st.text_input("Snowflake Account",  help="Enter the Snowflake Account")
log_table_name = st.text_input("Log Table Name", value="log_table", help="Enter the Log Table Name")

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
