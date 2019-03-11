from django.shortcuts import render
from django.http import HttpResponse

class Crystal:
    def __init__(self, name, type, description, healingproperties):
        self.name = name
        self.type = type
        self.description = description
        self.healingproperties = healingproperties

crystals = [
    Crystal('Selenite', 'The Master', 'This master mineral is one of the only healing crystals that does not need to be charged and can actually be used to cleanse and recharge other crystals. It is the most abundant crystal, and is found in ancient evaporated salt lakes and seas, and can be found from Mexico to Brazil and beyond.', 'Back-Problems-and-Pain, Bone-Disorders-and-Health, Bone-Strengthening, Cancer, Epilepsy, Health-and-Healing, Infection, Insomnia, Muscular/Skeletal, PMS, Psoriasis, Sleep, Spinal-Strengthening, Spine-Health, Tumors-and-Growths, Ulcers, Chaos, Forgiveness, Harmony, Honesty, Positive-Energy, Reducing-Stress-or-Tension, Self-Confidence-and-Self-Worth'),
    Crystal('Aventurine', 'The Stone of Opportunity', 'Known for amplifying luck, prosperity and abundance, aventurine is a good stone to take with you if you’re planning to gamble in Las Vegas. A variety of quartz, this stone attracts luck and assists in the successful application of new opportunities.', 'Eye-Disorders-and-Infections, Healing, Health-and-Healing, Heart, Vision, Anxiety, Calming, Emotional-Body-Purification, Emotional-Healing, Emotional-Trauma, Increase-Positive-Energy, Oversensitive, Positive-Energy, Rage-Diffusing-or-Release, Reducing-Stress-or-Tension, Soothing, Abundance, Devic-and-Nature-Realm-Communication-and-Connection, Healing'),
    Crystal('Moonstone', 'The Stabilizer', 'Deeply linked to the feminine and the moon, moonstone is a perfect stone to gracefully create harmony within and strengthen intuition. It was the stone of Gods and Goddesses in ancient India, and is seen as sacred and regal.', 'Arthritis, Birthing Problems and Health, Breast Health, Circulatory Problems, Edema, Headache and Migraine Relief, Health and Healing, Infertility, Insect Bites, Insomnia, Menopause, Menstrual Cramps and Menstruation, Multiple Sclerosis, Muscular/Skeletal, Pancreas Health, Pituitary Gland, PMS, Pregnancy, Stomach Problems/Constipation/Diarrhea, Anger Diffusing or Release, Centering, Composure, Emotional Balance, Emotional Healing, Fear of Dark, Happiness, Harmony, Hope, Nurture, Positive Energy')
]

def home(request):
    return HttpResponse('<h1>╲┏━┳━━━━━━━━┓╲╲<br>╲┃◯┃╭┻┻╮╭┻┻╮┃╲╲<br>╲┃╮┃┃╭╮┃┃╭╮┃┃╲╲<br>╲┃╯┃┗┻┻┛┗┻┻┻┻╮╲<br>╲┃◯┃╭╮╰╯┏━━━┳╯╲<br>╲┃╭┃╰┏┳┳┳┳┓◯┃╲╲<br>╲┃╰┃◯╰┗┛┗┛╯╭┃╲╲</h1>')

def about(request):
    return render(request, 'about.html')

def crystals_index(request):
    return render(request, 'crystals/index.html', { 'crystals': crystals })