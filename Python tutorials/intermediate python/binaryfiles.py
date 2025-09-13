with open (r"C:\Users\Pranmaya Niroula\Pictures\Screenshots\Screenshot 2024-09-03 084750.png","rb") as f:
    with open ("screenshot_copy.png","wb") as wf:
        wf.write(f.read())

#THIS WILL READ THE SCREENSHOT AND IN THE OUTPUT IT WILL DISPLAY THE SCREENSHOT
#IN THIS WAY WE CAN WORK WITH THE BINARY FILES