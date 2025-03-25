import asyncio
import sys

async def convert(file):
    print(f"🎥 Converting {file}")

    process = await asyncio.create_subprocess_exec(
        "pandoc", "-f", "mediawiki", "-t", "markdown", "-o", f"{file[:-4]}.md", file,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    stdout, stderr = await process.communicate()

    await asyncio.sleep(1)

    if process.returncode == 0:
        print(f"✅ {file} converted")
    else:
        print(f"❌ {file} not converted")

async def main():
    await convert(sys.argv[1])

asyncio.run(main())    