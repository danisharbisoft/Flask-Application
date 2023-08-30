from flask_app.models.user import User


def create_user(bcrypt, form, db):
    hashed_password = password_generation_for_reg(bcrypt, form)
    new_user = User(username=form.username.data, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()


def select_user(username: str):
    user = User.query.filter_by(username).first()
    return user


def password_check_for_login(user, bcrypt, entered_password):
    if user:
        if bcrypt.check_password_hash(user.password, entered_password):
            return True
        else:
            return False


def password_generation_for_reg(bcrypt, form):
    return bcrypt.generate_password_hash(form.password.data).decode('utf-8')


def error_handling(type):
    if type == 'password':
        return "Incorrect Password"

    elif type == 'user':
        return "User Does not Exist!"
