from django.db import models
from django.utils import timezone
import random

# Create your models here.
class GuessNumbers(models.Model):
    name = models.CharField(max_length=24)
    text = models.CharField(max_length=255)
    lottos = models.CharField(max_length=255, default='[1,2,3,4,5,6]')
    num_lotto = models.IntegerField(default=5)
    update_date = models.DateTimeField()

    def generate(self):
        self.lottos = ""
        origin = list(range(1,46))

        for _ in range(0, self.num_lotto):
            random.shuffle(origin)
            guess = origin[:6]
            guess.sort()
            # sort는 저희가 아까 shell 에서만 잠시 해봤던 것이고 실제로 sort 후 DB에 저장되지 않았어요! DB에 저장하려면 models.py 에 있는 Class.object.save() 함수가 실행되어야 합니다!
            self.lottos += str(guess) +'\n' # 나중에 처리하는 것보다 여기서 줄바꾸는게 더 편함
        self.update_date = timezone.now()
        self.save()  # sql의 commit 개념 / 보통은 밖에서 views.py에서 처리

    def __str__(self):
        return "pk {} : {} - {}".format(self.pk, self.name, self.text) # pk는 자동생성
