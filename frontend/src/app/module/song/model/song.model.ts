export interface SongSummary {
    id: string;
    title: string;
    artist: string;
}

export interface Song {
    id: string;
    title: string;
    artist: string;
    lyrics: string;
    countryList: Array<string>;
}