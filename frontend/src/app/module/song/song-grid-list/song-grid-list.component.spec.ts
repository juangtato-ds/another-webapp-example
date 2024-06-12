import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SongGridListComponent } from './song-grid-list.component';

describe('SongGridListComponent', () => {
  let component: SongGridListComponent;
  let fixture: ComponentFixture<SongGridListComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SongGridListComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SongGridListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
