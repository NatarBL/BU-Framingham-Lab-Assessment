# Exam class tracks individual appointments
class Exam:      
    def __init__(self, participant_id, ranid, date, days_from_exam_one, contents, src, dst, is_confirmed):
        self.participant_id = participant_id
        self.ranid = ranid
        self.date = date
        self.days_from_exam_one = days_from_exam_one
        self.contents = contents
        self.src = src
        self.dst = dst
        self.is_confirmed = is_confirmed

    def get_participant_id(self):
        return self.participant_id

    def get_ranid(self):
        return self.ranid

    def get_date(self):
        return self.date

    def get_days_from_exam_one(self):
        return self.days_from_exam_one

    def get_contents(self):
        return self.contents

    def get_src(self):
        return self.src

    def get_dst(self):
        return self.dst

    def get_is_confirmed(self):
        return self.is_confirmed