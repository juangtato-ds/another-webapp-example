import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SongArtistGridComponent } from './song-artist-grid.component';

describe('SongArtistGridComponent', () => {
  let component: SongArtistGridComponent;
  let fixture: ComponentFixture<SongArtistGridComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SongArtistGridComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SongArtistGridComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
