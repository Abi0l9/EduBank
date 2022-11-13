from models import db, School, Pupil, Teller

##


def save(data):
    db.session.add(data)
    db.session.commit()
    db.session.close()


def close():
    db.session.close()


def rollback():
    db.session.rollback()
    db.session.close()


def get_id_name(par):
    if par == "schools":
        schools = [{"id": school[0], "name": school[1]}
                   for school in db.session.query(School.id, School.name).all()]
        return schools
    elif par == "pupils":
        pupils = [{"id": pupil[0], "name": pupil[1]}
                  for pupil in db.session.query(Pupil.id, Pupil.name).all()]
        return pupils


def get_students_record(id):
    records = []
    global school_id
    global school_name

    query = db.session.query(School.id, School.name, Pupil.id, Pupil.name).join(
        School, Pupil.school_id == School.id).group_by(School.id, Pupil.id).all()

    for data in query:

        if data[0] == id:
            records.append({"id": data[2], "name": data[3]})
            school_id = data[0]
            school_name = data[1]
        # else:
        #     return (records, {"id": "", "name": ""})
    return (records, {"id": school_id, "name": school_name})
