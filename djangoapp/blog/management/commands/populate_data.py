from blog.models import Post
from django.core.management.base import BaseCommand
import random 
from blog.models import Category

class Command(BaseCommand):
    def handle(self, *args, **options):
         Post.objects.all().delete()
         title = [
  "Raspberry Delight",
  "Whispers of the Night Sky",
  "The Misty Mystery",
  "Rocky Shore Waves",
  "Vintage Wall Decor",
  "Calm Beach Morning",
  "The Bus Journey",
  "The Peace of Silence in Nature",
  "The Silent Damage Behind Crackers",
  "Night City Lights",
  "Working Setup",
  "Sunrise Adventure"
];

         content = [
  "A fresh look at the vibrant beauty of raspberries—bright, juicy, and full of natural charm. This post explores their color, texture, and the simple joy these tiny fruits bring to everyday moments.",
  
  "A peaceful night under a star-filled sky, where shadows and silence blend together. This post reflects on calm moments, slow thoughts, and the stillness that makes the night feel beautifully alive.",
  
  "A soft, mist-filled scene that hides details while revealing mood. This post explores mystery in nature, gentle fog, and the way hazy moments create emotion, depth, and quiet curiosity.",
  
  "The power and rhythm of waves crashing against rocky shores. This post captures coastal energy, natural motion, and the calming yet dramatic blend of water and stone.",
  
  "A warm, aesthetic look at vintage wall art and decor. This post highlights nostalgic textures, soft tones, and how classic elements can completely transform the feel of any space.",
  
  "A peaceful morning by the beach with calm waves and warm light. This post explores refreshing beginnings, slow mornings, and the soothing charm of seaside calmness.",
  
  "A simple journey captured through a bus window, showing life in motion. This post reflects on everyday travel, quiet moments on the road, and thoughts that arise while passing by the world.",
  
  "A moment of absolute peace found in nature’s gentle silence. This post explores stillness, soft landscapes, and how quiet places help reset the mind and soothe the heart.",
  
  "Crackers create momentary excitement but leave lasting pollution—smoke, toxic chemicals, loud noise, and air damage. This post highlights their hidden impact on health, environment, and why mindful celebrations matter more than temporary sparkle.",
  
  "The lively glow of a city at night, filled with lights and movement. This post explores urban energy, nighttime perspectives, and the beauty hidden in fast-paced city life.",
  
  "A cozy workspace that inspires creativity and focus. This post explores productivity, clean setups, calming elements, and how the right environment supports better thinking and work.",
  
  "A fresh sunrise symbolizing new beginnings. This post captures the beauty of early light, morning air, and the hopeful feeling that comes with every brand-new start."
] 

         img = [
        "https://picsum.photos/id/102/600/400",
        "https://picsum.photos/seed/science-discovery/600/500",
        "https://picsum.photos/seed/eco-nature/600/500",
        "https://picsum.photos/seed/food-lifestyle/600/500",
        "https://picsum.photos/seed/food-lifestyle/600/500",
        "https://picsum.photos/seed/robotics/600/400",
        "https://picsum.photos/seed/robotics/600/400",
        "https://picsum.photos/seed/psychology/600/400",
        "https://picsum.photos/seed/climatechange/600/400",
        "https://picsum.photos/seed/chemistry/600/400",
        "https://picsum.photos/seed/agriculture/600/400",
        "https://picsum.photos/seed/web-development/600/400"
         ]
         
         categories = Category.objects.all()
         
         for t , c, i in zip(title,content,img):
            category = random.choice(categories)
            Post.objects.create(title = t,content = c,img = i,category = category)
         self.stdout.write(self.style.SUCCESS('Completed inserting data'))

         def __str__(self):
            return self.title
