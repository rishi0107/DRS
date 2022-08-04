video=capture video from file
play(speed){
    select and import video;
    Frame= get video's first frame ;
    Frame= set video's (first+ speed) frame ;
    grabbed;
    Frame= video.read;\
    resize video according to frame;
    reset color in RGB format;
    Display Frame in canvas;

}