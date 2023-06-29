from easy_pil import Editor, load_image_async, Font
from PIL import Image
import discord
from discord import File

async def edits(member: discord.Member, background_image_filename, text: str):
  
  background_image = Image.open(background_image_filename).convert("RGB")
  
  background = Editor(background_image)
  profile_image = await load_image_async(str(member.avatar.url))
  
  profile_image = profile_image.convert("RGB")
  
  profile = Editor(profile_image).resize((400, 400)).circle_image()
  
  poppins_small = Font.poppins(size=40, variant="light")
  poppins = Font.poppins(size=72, variant="bold")

  
  background.paste(profile, (780, 330))
  background.ellipse((780, 330), 400, 400, outline="white", stroke_width=8)

  
  background.text((960, 770), f"{text} ", color="white", font=poppins, align="center")
  background.text((960, 860), f"{member.name}#{member.discriminator}", color="white", font=poppins_small, align="center")
  file = File(fp=background.image_bytes, filename="hking.jpg")
  return file

