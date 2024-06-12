import { ChangeDetectionStrategy, Component } from '@angular/core';

@Component({
  selector: 'app-floating-buttons',
  standalone: true,
  imports: [],
  template: `<div class="floating-actions">
  <div class="floating-buttons">
    <ng-content></ng-content>
  </div>
</div>`,
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class FloatingButtonsComponent {

}
