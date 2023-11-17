import BingImageCreator as bic
import asyncio

KEY = "12nnIQEq7Js0dn7Yvn4n7BO4x7p66Q3eHSWSjE8Zgc_K50EvkY0aCzaAFv9RAg2XYwRP96LflGk0t8dIejGgmb0iiszABLSDvR5ctG8Gmw4azYReZ8gTAziHLiFA5XBKX4EM3XLs2C3efiprqi7__GaCfk7An3VZpmpvzfybgujwmWiIYn7yNgPHkZXaiN74eyrsJ5UsBBPBWO7mEQ_jvlCtXgwfg0yy10Q4coACo1AY"
OUTPUT_DIR = "backend/images"

imagegen = bic.ImageGenAsync(auth_cookie=KEY)
loop = asyncio.get_event_loop()
task = imagegen.get_images("Medieval style night on a stormy beach painting")

links = loop.run_until_complete(task)
print(links)

#loop.run_until_complete(asyncio.gather(imagegen.save_images(links, output_dir=OUTPUT_DIR)))
loop.close()

