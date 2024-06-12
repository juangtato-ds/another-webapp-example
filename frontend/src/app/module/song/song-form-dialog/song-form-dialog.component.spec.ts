import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SongFormDialogComponent } from './song-form-dialog.component';

describe('SongFormDialogComponent', () => {
  let component: SongFormDialogComponent;
  let fixture: ComponentFixture<SongFormDialogComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SongFormDialogComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SongFormDialogComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
