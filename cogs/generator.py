import names
import string
import random
import discord
import asyncio
from discord.ext import commands
# importing all of the libraries used for the discord bot and the code

class Generator(commands.Cog):
  def __init__(self, bot):
    
    self.bot = bot
    self.password = "PasPolar12#"
    self.random = random.SystemRandom()
    self._alpha_list = list(string.ascii_letters + string.digits)
    self.createlink = "https://www.jcpenney.com/createaccount"
    
    # initiating all of the variables which will the used through all all of the code

  async def get_email(self):
    superb = self.random.choices(self._alpha_list, k=self.random.randint(7,11))
    return "".join(superb) + self.random.choice(['@dropoutsolutions.com'])
    
    # this basically generates a random string using two libraries: string and random
    # it then adds your domain to the end

  async def get_number(self):
      number = "408"
    
      for x in range(7):
        number += str(random.randint(1,9))
        
      return number
  # phone number generating
  # runs a loop 7 times to get the last 7 digits of a phone number after 408
    
  @commands.command(aliases=['gen','g'])
  async def generate(self, ctx, count=1):
  # making the discord bot generate command

    counter = 1
    # if you do `-g 5` it will run this loop 5 times
    for x in range(count):
      email = self.random.choice([await self.get_email() for x in range(10)])
      
      # cool variable because if you want to generate 5 emails, the bot will create 50 emails and choose a random 5 from those so its super super random
      
      # this line above calls the get_email function which creates the email
      name = names.get_full_name(gender='male')
      # this uses a library which creates the name for you

      # makes 10 numbers and gets a random one
      number = [await self.get_number() for x in range(10)]
      chosen = random.choice(number)
      
      embed = discord.Embed(title=f"Generated Account {counter}", description=f"Email: `{email}`\nPassword: `{self.password}`\nNumber: `{chosen}`\nName: `{name}`", timestamp = discord.utils.utcnow())
      
      # creates the message the bot will send with all of the information
      numcounter = 1
      formatted = ""
      
      for x in range(len(number)):
        
        value = number[numcounter-1]
        if x == chosen:
          value = f"<{number[numcounter-1]}>"
          
        if numcounter < 10:
          formatted += f"{str(numcounter)}.  {value}\n"
          
        else:
          formatted += f"{str(numcounter)}. {value}\n"
        numcounter += 1
      # basically just formatting all of the phone numbers
        
        
      embed.add_field(name = "\nGenerated Info", value = f"```md\nPhone Numbers: \n{formatted}\nEmail: \n1.  {email}```\n[__Click to log in__](https://www.jcpenney.com/signin \"Hovertext\")")

      # embed fields
      print(f"\n \nGenerated Account {counter}")
      print(f"Email: {email}\nPassword: {self.password}\nNumber: {chosen}\nName: {name}")
      
      await ctx.send(embed=embed)
      # sends the message
      counter += 1
      await asyncio.sleep(2)
      # sleeps

async def setup(bot):
  await bot.add_cog(Generator(bot))