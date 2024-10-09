import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import requests
import asyncio

from scraper import Marketplace

load_dotenv()

# Initialize the bot
intents = discord.Intents.default()
intents.message_content = True
intents.typing = False
intents.presences = False
bot = commands.Bot(command_prefix='!', intents=intents)

#grab token

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')


@bot.command(name='marketplace')
async def marketplace(ctx):
    # Prompt for each parameter
    await ctx.send("Please enter the city:")
    city = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
    
    await ctx.send("Please enter the product:")
    product = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
    
    await ctx.send("Please enter the minimum price:")
    minimum = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
    
    await ctx.send("Please enter the maximum price:")
    maximum = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
    
    await ctx.send("Please enter the days listed:")
    listed = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
    
    # Pass the collected parameters to the Marketplace function
    try:
        
        result_data = Marketplace(city.content, product.content, int(minimum.content), int(maximum.content), int(listed.content))
        await ctx.send(f"Marketplace search results:")
        
        for data in result_data:
            await ctx.send(data['text'])
            await ctx.send(data['url'])
            
        await ctx.send(f"End of output")
        
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")


@bot.command(name='marketplacetest')
async def marketplacetest(ctx):
    # Pass the collected parameters to the Marketplace function
    try:
        result_data = Marketplace('houston', 'rsx', int(0), int(8000), int(7))
        await ctx.send(f"Marketplace search results:")
        
        for data in result_data:
            await ctx.send(data['text'])
            await ctx.send(data['url'])
        await ctx.send(f"End of output")
        
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")



# Run the bot with the token
bot.run(DISCORD_TOKEN)