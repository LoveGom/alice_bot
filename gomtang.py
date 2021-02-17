import asyncio
import discord
import psutil
import pybithumb
from discord.ext import commands
from datetime import datetime
from gpiozero import CPUTemperature



bot = commands.Bot(command_prefix='gt.')

@bot.event
async def on_ready():
    print(f'{bot.user.name} 에 성공적으로 로그인했습니다') #봇이 성공적으로 작동하고 있다는 메시지를 콘솔에 출력
    print(f'봇의 ID는 다음과 같아요 "{bot.user.id}"')
    date = datetime.now()
    while(True):        
        await bot.change_presence(activity = discord.Streaming(name = "gt.도움", url= "https://www.twitch.tv/bookguk_gom")) #디스코드 rich presence
        await asyncio.sleep(5)
        await bot.change_presence(activity = discord.Streaming(name = f"ver. BATA {date.year}. {date.month}. {date.day}. ", url= "https://www.twitch.tv/bookguk_gom"))
        await asyncio.sleep(5)
@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms') #핑 계산
@bot.command()
async def lord(ctx): #로오오드 타찬카...
    await ctx.send('https://r6skin.com/wp-content/uploads/2019/02/r6s-bundle_tachankamedieval_960x540_323504.jpg')
    await ctx.send('https://media.altchar.com/prod/images/940_530/gm-fe37e26f-f3bd-42b8-9be7-2b2c3ee7e692-lordtachankarework.jpeg')
    await ctx.send('https://cdn.player.one/sites/player.one/files/styles/lg/public/2020/03/13/rainbowsixsiegetachanka-vg247.jpg') 
@bot.command()
async def leave(ctx): #통화방에서 나가기
    await ctx.voice_client.disconnect()
@bot.command()
async def stop(ctx):  #와! 됐당!
    guild = ctx.guild
    voice_client: discord.VoiceClient = discord.utils.get(bot.voice_clients, guild=guild)
    voice_client.stop()
    await ctx.send('재생하고 있던 음악을 멈췄어요.')
@bot.command()
async def join(ctx): #통화방 입장
    channel = ctx.author.voice.channel
    await channel.connect()
    await ctx.send(f'"**{channel}**"에 성공적으로 연결했어요.')
@bot.command()
async def play(ctx): #mp3.mp3 재생
    guild = ctx.guild
    voice_client: discord.VoiceClient = discord.utils.get(bot.voice_clients, guild=guild)
    audio_source = discord.FFmpegPCMAudio('mp3.mp3')
    if not voice_client.is_playing():
        voice_client.play(audio_source, after=None)
@bot.command() #marigold.mp3 재생
async def play_marigold(ctx):
    guild = ctx.guild
    voice_client: discord.VoiceClient = discord.utils.get(bot.voice_clients, guild=guild)
    audio_source = discord.FFmpegPCMAudio('marigold.mp3')
    if not voice_client.is_playing():
        voice_client.play(audio_source, after=None)
        channel = ctx.author.voice.channel
        await ctx.send(f':white_check_mark: "**{channel}**"에서 "**Marigold**"를 재생할께요!')
@bot.command() #magnolia.mp3 재생
async def play_magnolia(ctx):
    guild = ctx.guild
    voice_client: discord.VoiceClient = discord.utils.get(bot.voice_clients, guild=guild)
    audio_source = discord.FFmpegPCMAudio('magnolia.mp3')
    if not voice_client.is_playing():
        voice_client.play(audio_source, after=None)
@bot.command() #도움말
async def 도움(ctx):
        embedVar = discord.Embed(title="도움말", description="명령어는 아래에서 확인하세요!", color=0x00ff00) #embed 초기 설정을 합니다
        embedVar.add_field(name="gt.ping", value="네트워크 지연시간을 표기합니다.", inline=False)
        embedVar.add_field(name="gt.join", value="음성 채팅으로 연결합니다.", inline=False)
        embedVar.add_field(name="gt.play", value="소비에트 연방 찬가를 고음질로 재생합니다.", inline=False)
        embedVar.add_field(name="gt.play_marigold", value="Margold - M2U 를 고음질로 재생합니다.", inline=False)
        embedVar.add_field(name="gt.play_magnolia", value="Magnolia - M2U 를 고음질로 재생합니다.", inline=False)
        embedVar.add_field(name="gt.leave", value="음성 채팅으로 부터 연결을 끊습니다.", inline=False)
        embedVar.add_field(name="gt.시세", value="(NEW) 비트코인 시세를 확인합니다.", inline=False)
        embedVar.add_field(name="gt.정보", value="(NEW) 현재 돌아가고 있는 서버의 상태를 확인합니다.", inline=False)
        embedVar.set_thumbnail(url="https://i.ibb.co/dW3kb01/dd1.png") #embed 썸네일을 지정합니다
        await ctx.send(embed=embedVar) #embed를 출력합니다
@bot.command() #시세
async def 시세(ctx):
    embedVar = discord.Embed(color=0x00ff00) #embed 초기 설정을 합니다
    btc = pybithumb.get_current_price("BTC") #각 코인의 시세를 받아와서 서로의 이름의 변수에 넣습니다
    eth = pybithumb.get_current_price("ETH") #//
    xrp = pybithumb.get_current_price("XRP") #//
    embedVar.add_field(name="비트코인", value=f"{btc} BTC(₿)", inline=False) #embed에 각각 변수를 넣습니다
    embedVar.add_field(name="이더리움", value=f"{eth} ETH(Ξ)", inline=False) #//
    embedVar.add_field(name="리플", value=f"{xrp} XRP", inline=False) #//

    embedVar.set_thumbnail(url="https://i.ibb.co/dW3kb01/dd1.png") #embed 썸네일을 지정합니다
    await ctx.send(embed=embedVar) #embed를 출력합니다
@bot.command()
async def 정보(ctx):
    memory = psutil.virtual_memory()
    avail = round(memory.available/1024**3, 1) #사용 가능한 메모리 계산
    percent = memory.percent #메모리 퍼센트 계산
    total = round(memory.total/1024**3, 1) # 총 메모리를 계산 후 소수점 1자리 까지만 반올림
    distotal = round(memory.total/1024**3) # "" 반올림 (소수점 X)
    cpu = CPUTemperature() #cpu 온도 확인
    embedVar = discord.Embed(title="정보", description="시스템 정보를 표시합니다.", color=0x90EE90) 
    embedVar.add_field(name="CPU 사용량 :", value=f"{psutil.cpu_percent()}% ({cpu.temperature}°C)", inline=False) #embed에 각각 변수를 넣습니다
    embedVar.add_field(name="메모리 사용량 :", value=f"{distotal}GB 중 {round(total - avail, 1)}GB 사용 중 ({avail}GB 사용 가능 ({percent}%))", inline=False)
    embedVar.set_thumbnail(url="https://i.ibb.co/dW3kb01/dd1.png")
    await ctx.send(embed=embedVar) #embed를 출력합니다

@commands.is_owner() #소유자만이 작동 가능
@bot.command()
async def fo(ctx):
        await ctx.send(':hand_splayed:')
        await ctx.bot.logout() #종료
bot.run('<token>') # 토큰을 입력해주세요!




