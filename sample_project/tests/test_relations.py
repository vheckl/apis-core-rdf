from django.test import TestCase
from django.core.exceptions import ValidationError
from sample_project.models import Person, Place, Group, BornIn, DiedIn, StudiedAt, LocatedIn, IsMarriedTo


class PersonRelationsTests(TestCase):
    def setUp(self):
        self.marie = Person.objects.create(forename="Marie", surname="Curie")
        self.pierre = Person.objects.create(forename="Pierre", surname="Curie")
        self.warsaw = Place.objects.create(label="Warsaw")
        self.paris = Place.objects.create(label="Paris")
        self.sorbonne = Group.objects.create(label="Sorbonne")

    def test_born_in(self):
        BornIn(subj=self.marie, obj=self.warsaw).save()

    def test_died_in(self):
        DiedIn(subj=self.marie, obj=self.paris).save()

    def test_studied_at(self):
        StudiedAt(subj=self.marie, obj=self.sorbonne).save()

    def test_located_in(self):
        LocatedIn(subj=self.sorbonne, obj=self.paris).save()

    def test_is_married_to(self):
        IsMarriedTo(subj=self.marie, obj=self.pierre).save()

    def test_born_in_wrong_object(self):
        with self.assertRaises(ValidationError):
            BornIn(subj=self.marie, obj=self.pierre).save()