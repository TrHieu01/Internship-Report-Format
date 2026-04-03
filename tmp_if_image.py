from PIL import Image, ImageDraw, ImageFont 
w,h=1400,240 
img=Image.new('RGB'),(w,h),(15,23,42) 
d=ImageDraw.Draw(img) 
text=\"if: always() ^&^& (needs.packer.result == 'success' ^|^| needs.packer.result == 'skipped') ^&^& (github.event_name == 'workflow_dispatch' ^|^| github.event.workflow_run.conclusion == 'success')\" 
font=None 
