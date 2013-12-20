def is_applicant(user):
    return user.groups.filter(name='applicant').count() == 1
