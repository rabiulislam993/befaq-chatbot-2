from django.db import models


MARHALA = (
    (1, "তাকমিল" ),
    (2, "ফযীলত" ),
    (3, "সানাবিয়া উলইয়া" ),
    # 5 number is missing in origin wifaqresult.com site! 
    (5, "মুতাওয়াসসিতাহ" ),
    (6, "ইবতিদাইয়্যাহ" ),
    (7, "হিফযুল কুরআন" ),
    (8, "ইলমুত তাজবীদ ওয়াল কিরাআত" ),
)

EXAM_YEARS = (
    (2015, '২০১৫'),
    (2016, '২০১৬'),
    (2017, '২০১৭'),
    (2018, '২০১৮'),
)


class Result(models.Model):
    student_roll = models.IntegerField()
    student_marhala = models.IntegerField(default=1, choices=MARHALA)
    exam_year = models.IntegerField(default=2018, choices=EXAM_YEARS)

    result = models.TextField(null=True, blank=True)

    def as_json(self):
        return {
            "roll" : self.student_roll,
            "marhala" : self.student_marhala,
            "year" : self.exam_year,
            "result" : self.result
        }

    def __str__(self):
        return "roll: {}, marhala:{}, year: {}".format(self.student_roll, 
                                                        self.student_marhala, 
                                                        self.exam_year)

    class Meta:
        ordering = ['-student_roll', 'student_marhala', '-exam_year']


class Proxy(models.Model):
    ip = models.TextField()

    def __str__(self):
        return "id: {}, ip: {}".format(self.id, self.ip)

    class Meta:
        ordering = ['-id']

