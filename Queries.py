insert_user_register_info = """
                            insert into login_users 
                            (name, email, password, registration_date)
                            values (%s, %s, %s, CURRENT_TIMESTAMP)
                            """