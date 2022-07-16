use yew::prelude::*;
mod video_struct;

#[function_component(App)]
fn app() -> Html 
{ 
    use video_struct::Video;

    let videos = vec!
    {
        Video
        {
            id: 1,
            title: "Building and breaking things".to_string(),
            speaker: "John Doe".to_string(),
            url: "https://youtu.be/PsaFVLr8t4E".to_string(),
        },
        Video
        {
            id: 2,
            title: "The development process".to_string(),
            speaker: "Jane Smith".to_string(),
            url: "https://youtu.be/PsaFVLr8t4e".to_string(),
        },
        Video
        {
            id: 3,
            title: "Web 7.0".to_string(),
            speaker: "Matt Miller".to_string(),
            url: "https://youtu.be/PsaFVLr8t4e".to_string(),
        },
        Video
        {
            id: 2,
            title: "Mouseless development".to_string(),
            speaker: "Tom Jerry".to_string(),
            url: "https://youtu.be/PsaFVLr8t4e".to_string(),
        },
    };

    let videos = videos.iter().map(|video| html!
                                  {
                                      <p>{format!("{}: {}", video.speaker, video.title)}</p>
                                  }).collect::<Html>();

    html!
    {
        <>
            <h1>{ "RustConf Explorer" }</h1>
            <div>
                <h3>{ "Videos to watch" }</h3>
                { videos }
            </div> 
        </>
    }
}

fn main() 
{
    yew::start_app::<App>();
}


