import bpy
import os

for file in os.listdir('./'):
    if (file[-4:] == ".mp4"):
        filepath = "F:\\Video test\\" + file
        name = file


area = bpy.context.area
area.type = 'SEQUENCE_EDITOR'


#Set Desired Screen Resolution and Aspect Ratio
bpy.context.scene.render.resolution_x = 1080
bpy.context.scene.render.resolution_y = 1920
bpy.context.scene.frame_start = 0


#Add Your Video
for file in os.listdir('F:\\Video test\\'):
    directory = "F:\\Video test\\"
    if (file[-4:] == ".mp4"):
        filepath = "F:\\Video test\\" + file
        name = file
        Output_path = f"F:\\Video test\\{name}"[0:-4]

        bpy.ops.sequencer.movie_strip_add(filepath=filepath, directory=directory, files=[{"name":name, "name":name}], relative_path=True, show_multiview=False, frame_start=0, channel=2, fit_method='FIT', set_view_transform=False, adjust_playback_rate=True, use_framerate=False)

        #Rotate Video to adjust
        video = bpy.context.scene.sequence_editor.sequences_all[name]
        video.transform.rotation = 4.71239
        
        width = video.elements[0].orig_width
        height = video.elements[0].orig_height
        
        if height == width:
            video.transform.scale_y = 0.75
            video.transform.scale_x = 0.75
        else:
            video.transform.scale_y = 1
            video.transform.scale_x = 1

        #Get number of frames
        number_of_frames = video.frame_final_duration

        #Add black background
        bpy.ops.sequencer.effect_strip_add(type='COLOR', frame_start=0, frame_end=number_of_frames, channel=1)


        #Output Settings
        bpy.context.scene.frame_end = number_of_frames - 1
        bpy.context.scene.render.image_settings.file_format = 'FFMPEG'
        bpy.context.scene.render.ffmpeg.codec = 'H264'
        bpy.context.scene.render.ffmpeg.format = 'MPEG4'
        bpy.context.scene.render.ffmpeg.constant_rate_factor = 'PERC_LOSSLESS'
        bpy.context.scene.render.filepath = Output_path

        #Render
        bpy.ops.render.render(animation=True)
        print(f"Video Rendered: {name}")

        #clear the sequencer
        bpy.ops.sequencer.select_all(action='SELECT')
        bpy.ops.sequencer.delete()
        
area.type = 'TEXT_EDITOR'