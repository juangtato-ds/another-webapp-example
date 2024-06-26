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

export interface SongForm {
    id?: string;
    artist: string;
    title: string;
}

export interface ArtistMap {
    [key: string]: Array<SongSummary>;
}