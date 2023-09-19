import discord
from discord.ext import commands

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

# Define a dictionary to map roles to categories
ticket_categories = {
    'developer': category id,  # Replace with the actual category ID
    'designer': category id,  # Replace with the actual category ID
    # Add more role-category mappings here
}

@bot.event
async def on_message(message):
    if message.channel.id == channel id:
        if message.content.startswith('!ticket'):
            await message.delete()
        elif not message.content.startswith('!ticket'):
            await message.delete()

    await bot.process_commands(message)

# Define a command to create a ticket
@bot.command()
async def ticket(ctx, role: str):
    # Check if the specified role is valid
    if role.lower() in ticket_categories:
        category_id = int(ticket_categories[role.lower()])
        category = discord.utils.get(ctx.guild.categories, id=category_id)
        
        if category:
            # Create a new text channel under the specified category
            channel = await ctx.guild.create_text_channel(
                f'{role}-ticket-{ctx.author.display_name}',
                category=category
            )

            # Define permissions for the channel
            overwrites = {
                ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
                ctx.author: discord.PermissionOverwrite(read_messages=True),
                ctx.guild.owner: discord.PermissionOverwrite(read_messages=True),
            }
            
            # Apply permissions to the channel
            for target, overwrite in overwrites.items():
                await channel.set_permissions(target, overwrite=overwrite)
            
            # Send a welcome message
            await channel.send(f"Welcome to your {role} ticket, {ctx.author.mention}!")

    else:
        await ctx.send("Invalid role. Use `!ticket put your role here` or `!ticket put your role here`.")

# Run the bot
bot.run("token here")  # Replace with your bot's token
