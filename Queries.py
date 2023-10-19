insert_user_register_info = """
                            insert into login_users 
                            (name, email, password, registration_date)
                            values (%s, %s, %s, CURRENT_TIMESTAMP);
                            """

select_user_password = "select password from login_users where email = %s"

select_user_email = "select email from login_users where email = %s"

update_user_password = "update login_users set password = %s where name = %s and email = %s"