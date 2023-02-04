from django.core.management import BaseCommand

# from catalog.models import Student
from catalog.models import Record


class Command(BaseCommand):
    def handle(self, *args, **options):

        jj=[

    #Zapolnim textom stranici-productov
        {"title": "crab1",
        "content": "The blue crab is a much-prized type of seafood that provides delicious tender meat that is mildly briny, with a subtle sweet undertone. It makes good eating on its own and also pairs well with a wide range of other flavors. This crab is likely to appeal to most people as it has no offensive or overpowering taste",
        "image": "records/crab.jpeg",
        "id_public": True},
        {"title": "onion",
        "content":  "The onion is likely native to southwestern Asia but is now grown throughout the world, chiefly in the temperate zones. Onions are low in nutrients but are valued for their flavour and are used widely in cooking. They add flavour to such dishes as stews, roasts, soups, and salads and are also served as a cooked vegetable",
        "image": "records/onion.jpeg",
        "id_public": True,
        },
        {"title": "lobster",
        "content": "This might be a misnomer. While it’s called American lobster, this species is found as far south as North Carolina in the US all the way to Labrador in northern Canada. In fact, in Canada, 97% of lobster fisheries are MSC certified. Known for its firm, sweet meat, American lobster holds up well to a variety of cooking styles, and no one can agree on whether the claw or tail meat is better!",
         "image": "records/th.jpeg",
         "id_public": True,
         }
        ]
        for i in jj:

            rec_2 = Record(title=i["title"], content=i["content"], image=i["image"], id_public=i["id_public"])
            rec_2.save()