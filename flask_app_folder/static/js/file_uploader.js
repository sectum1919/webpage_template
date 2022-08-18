
/********************************************
* global settings
********************************************/
FilePond.registerPlugin(
    // validates files based on input type
    FilePondPluginFileValidateType,
    // previews the image
    FilePondPluginImagePreview,
    // previews media like audio or video
    FilePondPluginMediaPreview,
);
/********************************************
* image uploader
********************************************/
image_pond = FilePond.create(
    document.getElementById('image_uploader'),
    {
        labelIdle: `Drag & Drop your picture or Copy & Paste`,
    },
);
image_pond.setOptions({
    server: {
        process: '/upload/image',
        revert: null,
    },
    acceptedFileTypes: ['image/png', 'image/jpg'],
    allowBrowse: false,
});
/********************************************
* image uploader
********************************************/
image_pond_browse = FilePond.create(
    document.getElementById('image_uploader_browse'),
    {
        labelIdle: `Drag & Drop your picture or Copy & Paste or Browse`,
    },
);
image_pond_browse.setOptions({
    server: {
        process: '/upload/image',
        revert: null,
    },
    acceptedFileTypes: ['image/png', 'image/jpg'],
    allowBrowse: true,
});
/********************************************
* audio uploader
********************************************/
audio_pond = FilePond.create(
    document.getElementById('audio_uploader'),
    {
        labelIdle: `Drag & Drop your audio or <span class="filepond--label-action">Browse</span>`,
        allowAudioPreview: true,
    },
);
audio_pond.setOptions({
    server: {
        process: '/upload/audio',
        revert: null,
    },
    acceptedFileTypes: ['audio/wav', 'audio/mp3'],
});
/********************************************
* video uploader
********************************************/
// only support what <video> support
// that means can't preview video of some specific encode format
video_pond = FilePond.create(
    document.getElementById('video_uploader'),
    {
        labelIdle: `Drag & Drop your video or <span class="filepond--label-action">Browse</span>`,
        allowVideoPreview: true,
    },
);
video_pond.setOptions({
    server: {
        process: '/upload/video',
        revert: null,
    },
    acceptedFileTypes: ['video/mpg', 'video/mp4'],
});