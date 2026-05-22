---
slug: mtpi-angular-ui-ux-detailed-specification
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 00-foundations/mtpi/MTPI Angular UI_UX_ Detailed Specification.md
  last_synced: '2026-03-20T17:17:22.858416Z'
---

MTPI Angular UI/UX: Detailed Specification
Revision: Web demo using Angular instead of vanilla JS
Target: Production-grade interactive validator with rich visualizations


Architecture Overview

Technology Stack

  Frontend Framework: Angular 17+ (standalone components)
  Build Tool: Angular CLI + Vite
  Styling: Tailwind CSS + Angular Material
  WASM Integration: @angular/platform-browser + custom WASM loader
  State Management: Angular Signals (built-in)
  Charts: D3.js + ngx-charts
  Animations: Angular Animations + GSAP
  Testing: Jasmine + Karma + Cypress



Project Structure

  packages/mtpi-angular/
  ├── angular.json
  ├── package.json
  ├── tsconfig.json
  ├── tailwind.config.js
  ├── src/
  │   ├── main.ts
  │   ├── index.html
  │   ├── styles.scss
  │   ├── app/
  │   │   ├── app.config.ts
  │   │   ├── app.routes.ts
  │   │   ├── app.component.ts
  │   │   │
  │   │   ├── core/
  │   │   │   ├── services/
  │   │   │   │   ├── mtpi-wasm.service.ts         # WASM bridge
  │   │   │   │   ├── validation.service.ts         # Validation logic
  │   │   │   │   ├── analytics.service.ts         # Usage tracking
  │   │   │   │   └── theme.service.ts              # Dark/light mode
  │   │   │   ├── models/
  │   │   │   │   ├── validation-result.ts
  │   │   │   │   ├── archetype.ts
│   │   │   │   └── certificate.ts
│   │   │   └── guards/
│   │   │       └── wasm-loaded.guard.ts
│   │   │
│   │   ├── features/
│   │   │   ├── validator/
│   │   │   │   ├── validator.component.ts
│   │   │   │   ├── validator.component.html
│   │   │   │   ├── validator.component.scss
│   │   │   │   └── components/
│   │   │   │       ├── input-panel/
│   │   │   │       ├── result-card/
│   │   │   │       ├── entropy-gauge/
│   │   │   │       └── factorization-tree/
│   │   │   │
│   │   │   ├── explorer/
│   │   │   │   ├── explorer.component.ts      # Batch exploration
│   │   │   │   └── components/
│   │   │   │       ├── range-scanner/
│   │   │   │       ├── heatmap-view/
│   │   │   │       └── histogram/
│   │   │   │
│   │   │   ├── archetypes/
│   │   │   │   ├── archetypes.component.ts
│   │   │   │   └── components/
│   │   │   │       ├── archetype-card/
│   │   │   │       ├── archetype-gallery/
│   │   │   │       └── comparison-view/
│   │   │   │
│   │   │   ├── playground/
│   │   │   │   ├── playground.component.ts     # Interactive experiments
│   │   │   │   └── components/
│   │   │   │       ├── factor-builder/
│   │   │   │       ├── entropy-simulator/
│   │   │   │       └── prime-lattice/
│   │   │   │
│   │   │   └── about/
│   │   │       ├── about.component.ts
│   │   │       └── components/
│   │   │           ├── math-explainer/
│   │   │           ├── timeline/
│   │   │           └── team/
│   │   │
│   │   ├── shared/
│   │   │   ├── components/
│   │   │   │   ├── header/
│   │   │   │   ├── footer/
│   │   │   │   ├── loading-spinner/
│   │   │   │   ├── error-display/
│   │   │   │   └── theme-toggle/
│   │   │   ├── directives/
│   │   │   │   ├── number-input.directive.ts
│   │   │   │   └── copy-to-clipboard.directive.ts
│   │   │   └── pipes/
│   │   │       ├── format-number.pipe.ts
│   │   │       ├── factorization.pipe.ts
 │   │   │       └── entropy-color.pipe.ts
 │   │   │
 │   │   └── assets/
 │   │       ├── wasm/
 │   │       │   └── mtpi_wasm_bg.wasm
 │   │       ├── data/
 │   │       │   ├── archetypes.json
 │   │       │   └── known-lawful.json
 │   │       └── images/
 │   │           └── multiplicity-logo.svg
 │   │
 │   └── environments/
 │       ├── environment.ts
 │       └── environment.prod.ts
 │
 └── cypress/
     ├── e2e/
     │   ├── validator.cy.ts
     │   ├── explorer.cy.ts
     │   └── archetypes.cy.ts
     └── support/




Design System

Color Palette

 // src/styles/variables.scss

 // Primary (Multiplicity Blue)
 $primary-50: #eff6ff;
 $primary-100: #dbeafe;
 $primary-200: #bfdbfe;
 $primary-300: #93c5fd;
 $primary-400: #60a5fa;
 $primary-500: #3b82f6; // Main brand color
 $primary-600: #2563eb;
 $primary-700: #1d4ed8;
 $primary-800: #1e40af;
 $primary-900: #1e3a8a;

 // Success (Lawful Green)
 $success-50: #f0fdf4;
 $success-500: #10b981;
 $success-700: #047857;

 // Danger (Unlawful Red)
 $danger-50: #fef2f2;
 $danger-500: #ef4444;
 $danger-700: #b91c1c;

 // Warning (Near-threshold Yellow)
 $warning-50: #fefce8;
 $warning-500: #eab308;
 $warning-700: #a16207;

 // Neutral (Background/Text)
 $gray-50: #f8fafc;
 $gray-100: #f1f5f9;
 $gray-200: #e2e8f0;
 $gray-300: #cbd5e1;
 $gray-400: #94a3b8;
 $gray-500: #64748b;
 $gray-600: #475569;
 $gray-700: #334155;
 $gray-800: #1e293b;
 $gray-900: #0f172a;


Typography

 // Font stack
 $font-family-base: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
 $font-family-mono: 'JetBrains Mono', 'Fira Code', 'Courier New', monospace;
 $font-family-display: 'Sora', 'Inter', sans-serif;

 // Font sizes (Tailwind-inspired)
 $text-xs: 0.75rem;     // 12px
 $text-sm: 0.875rem; // 14px
 $text-base: 1rem;      // 16px
 $text-lg: 1.125rem; // 18px
 $text-xl: 1.25rem;     // 20px
 $text-2xl: 1.5rem;     // 24px
 $text-3xl: 1.875rem; // 30px
 $text-4xl: 2.25rem; // 36px
 $text-5xl: 3rem;      // 48px


Spacing System

 // Consistent 8px grid
 $space-0: 0;
 $space-1: 0.25rem; // 4px
 $space-2: 0.5rem; // 8px
 $space-3: 0.75rem; // 12px
 $space-4: 1rem;     // 16px
 $space-5: 1.25rem; // 20px
 $space-6: 1.5rem; // 24px
 $space-8: 2rem;     // 32px
 $space-10: 2.5rem; // 40px
 $space-12: 3rem;    // 48px
 $space-16: 4rem;    // 64px
Component Specifications

1. Header Component
Purpose: Global navigation + branding

File: src/app/shared/components/header/header.component.ts

  import { Component, signal } from '@angular/core';
  import { CommonModule } from '@angular/common';
  import { RouterLink, RouterLinkActive } from '@angular/router';
  import { MatToolbarModule } from '@angular/material/toolbar';
  import { MatButtonModule } from '@angular/material/button';
  import { MatIconModule } from '@angular/material/icon';
  import { ThemeToggleComponent } from '../theme-toggle/theme-toggle.component';

  @Component({
    selector: 'app-header',
    standalone: true,
    imports: [
      CommonModule,
      RouterLink,
      RouterLinkActive,
      MatToolbarModule,
      MatButtonModule,
      MatIconModule,
      ThemeToggleComponent,
    ],
    template: `
      <mat-toolbar color="primary" class="header">
        <div class="header-container">
          <!-- Logo + Branding -->
          <a routerLink="/" class="brand">
            <img src="assets/images/multiplicity-logo.svg" alt="Multiplicity" class="logo"
            <span class="brand-text">MTPI</span>
            <span class="version">v{{ version }}</span>
          </a>

         <!-- Navigation -->
         <nav class="nav">
           <a routerLink="/validator" routerLinkActive="active" mat-button>
             <mat-icon>check_circle</mat-icon>
             Validator
           </a>
           <a routerLink="/explorer" routerLinkActive="active" mat-button>
             <mat-icon>explore</mat-icon>
             Explorer
           </a>
           <a routerLink="/archetypes" routerLinkActive="active" mat-button>
             <mat-icon>star</mat-icon>
             Archetypes
           </a>
           <a routerLink="/playground" routerLinkActive="active" mat-button>
             <mat-icon>science</mat-icon>
             Playground
        </a>
        <a routerLink="/about" routerLinkActive="active" mat-button>
          <mat-icon>info</mat-icon>
          About
        </a>
      </nav>

      <!-- Actions -->
      <div class="actions">
        <app-theme-toggle />
        <a href="https://github.com/MultiplicityFoundation/Meta-Theorem"
           target="_blank"
           mat-icon-button
           aria-label="GitHub">
          <mat-icon>code</mat-icon>
        </a>
      </div>
    </div>
  </mat-toolbar>
`,
styles: [`
  .header-container {
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 100%;
    max-width: 1400px;
    margin: 0 auto;
    padding: 0 1rem;
  }

 .brand {
   display: flex;
   align-items: center;
   gap: 0.75rem;
   text-decoration: none;
   color: inherit;
   transition: opacity 0.2s;

     &:hover {
       opacity: 0.8;
     }
 }

 .logo {
   height: 32px;
   width: 32px;
 }

 .brand-text {
   font-family: var(--font-display);
   font-size: 1.5rem;
   font-weight: 700;
   letter-spacing: -0.02em;
 }
     .version {
       font-size: 0.75rem;
       opacity: 0.7;
       font-weight: 500;
     }

     .nav {
       display: flex;
       gap: 0.25rem;

         a.active {
           background: rgba(255, 255, 255, 0.1);
         }
     }

     .actions {
       display: flex;
       align-items: center;
       gap: 0.5rem;
     }

      @media (max-width: 768px) {
        .nav {
          display: none; // Collapse to hamburger menu
        }
      }
    `]
  })
  export class HeaderComponent {
    version = '0.1.0';
  }



2. Validator Input Panel
Purpose: Primary number input + validation trigger

File: src/app/features/validator/components/input-panel/input-panel.component.ts

  import { Component, output, signal, computed } from '@angular/core';
  import { CommonModule } from '@angular/common';
  import { FormsModule } from '@angular/forms';
  import { MatFormFieldModule } from '@angular/material/form-field';
  import { MatInputModule } from '@angular/material/input';
  import { MatButtonModule } from '@angular/material/button';
  import { MatIconModule } from '@angular/material/icon';
  import { MatChipsModule } from '@angular/material/chips';

  @Component({
    selector: 'app-input-panel',
    standalone: true,
    imports: [
      CommonModule,
      FormsModule,
      MatFormFieldModule,
  MatInputModule,
  MatButtonModule,
  MatIconModule,
  MatChipsModule,
],
template: `
  <div class="input-panel">
    <div class="input-card">
      <h2 class="title">Validate a Number</h2>
      <p class="subtitle">
        Enter any positive integer to validate its lawfulness under MTPI
      </p>

     <!-- Main input -->
     <mat-form-field appearance="outline" class="number-input">
       <mat-label>Number</mat-label>
       <input
         matInput
         type="text"
         [(ngModel)]="inputValue"
         (keyup.enter)="handleValidate()"
         [placeholder]="randomExample()"
         #numberInput
       />
       <mat-icon matPrefix>tag</mat-icon>
       <button
         mat-icon-button
         matSuffix
         (click)="clearInput()"
         *ngIf="inputValue"
         aria-label="Clear">
         <mat-icon>close</mat-icon>
       </button>
       <mat-hint *ngIf="inputError()" class="error-hint">
         {{ inputError() }}
       </mat-hint>
     </mat-form-field>

     <!-- Action buttons -->
     <div class="actions">
       <button
         mat-raised-button
         color="primary"
         (click)="handleValidate()"
         [disabled]="!isValidInput() || loading()"
         class="validate-btn">
         <mat-icon>check_circle</mat-icon>
         {{ loading() ? 'Validating...' : 'Validate' }}
       </button>

       <button
         mat-button
         (click)="randomNumber()"
         [disabled]="loading()">
         <mat-icon>shuffle</mat-icon>
         Random
       </button>
     </div>

     <!-- Quick presets -->
     <div class="presets">
       <span class="presets-label">Quick examples:</span>
       <mat-chip-set>
         @for (preset of presets; track preset.value) {
           <mat-chip
             (click)="selectPreset(preset.value)"
             [disabled]="loading()">
             {{ preset.label }}
           </mat-chip>
         }
       </mat-chip-set>
     </div>
   </div>

    <!-- History (recent validations) -->
    @if (history().length > 0) {
      <div class="history-card">
        <h3 class="history-title">Recent</h3>
        <div class="history-list">
          @for (item of history(); track item.n) {
            <button
              class="history-item"
              (click)="selectFromHistory(item.n)">
              <span class="history-number">{{ item.n | number }}</span>
              <span class="history-badge" [class.lawful]="item.lawful">
                {{ item.lawful ? '✓' : '✗' }}
              </span>
            </button>
          }
        </div>
      </div>
    }
  </div>
`,
styles: [`
  .input-panel {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
  }

 .input-card {
   background: var(--surface);
   border-radius: 12px;
   padding: 2rem;
   box-shadow: var(--shadow-md);
 }

 .title {
   font-size: 1.875rem;
   font-weight: 700;
   margin-bottom: 0.5rem;
    color: var(--text-primary);
}

.subtitle {
  color: var(--text-secondary);
  margin-bottom: 2rem;
}

.number-input {
  width: 100%;
  font-size: 1.25rem;

    ::ng-deep input {
      font-family: var(--font-mono);
      font-size: 1.5rem;
      letter-spacing: 0.05em;
    }
}

.error-hint {
  color: var(--danger-500);
}

.actions {
  display: flex;
  gap: 1rem;
  margin-top: 1rem;
}

.validate-btn {
  flex: 1;
  height: 48px;
  font-size: 1.1rem;
}

.presets {
  margin-top: 1.5rem;
  padding-top: 1.5rem;
  border-top: 1px solid var(--border);
}

.presets-label {
  font-size: 0.875rem;
  color: var(--text-secondary);
  margin-bottom: 0.75rem;
  display: block;
}

mat-chip {
  cursor: pointer;
  transition: transform 0.2s;

    &:hover {
      transform: translateY(-2px);
    }
}
.history-card {
  background: var(--surface);
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: var(--shadow-sm);
}

.history-title {
  font-size: 1rem;
  font-weight: 600;
  margin-bottom: 1rem;
  color: var(--text-secondary);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.history-list {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.history-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.75rem 1rem;
  background: var(--background);
  border: 1px solid var(--border);
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.2s;

    &:hover {
      border-color: var(--primary-500);
      background: var(--primary-50);
    }
}

.history-number {
  font-family: var(--font-mono);
  font-weight: 600;
}

.history-badge {
  width: 24px;
  height: 24px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.875rem;
  background: var(--danger-100);
  color: var(--danger-700);
      &.lawful {
        background: var(--success-100);
        color: var(--success-700);
      }
    }
  `]
})
export class InputPanelComponent {
  // Signals
  inputValue = signal('');
  loading = signal(false);
  inputError = signal<string | null>(null);
  history = signal<Array<{ n: number; lawful: boolean }>>([]);

 // Computed
 isValidInput = computed(() => {
   const val = this.inputValue().trim();
   if (!val) return false;
   const num = parseInt(val, 10);
   return !isNaN(num) && num > 0 && num <= Number.MAX_SAFE_INTEGER;
 });

 // Outputs
 validate = output<number>();

 presets = [
   { label: '42 (Triadic)', value: 42 },
   { label: '210 (Tetrad)', value: 210 },
   { label: '2310 (Pentad)', value: 2310 },
   { label: '1024 (Synthetic)', value: 1024 },
 ];

 randomExample(): string {
   const examples = [42, 210, 2310, 7919, 12345];
   return examples[Math.floor(Math.random() * examples.length)].toString();
 }

 clearInput(): void {
   this.inputValue.set('');
   this.inputError.set(null);
 }

 handleValidate(): void {
   if (!this.isValidInput()) {
     this.inputError.set('Please enter a valid positive integer');
     return;
   }

     const num = parseInt(this.inputValue(), 10);
     this.inputError.set(null);
     this.validate.emit(num);
 }

 randomNumber(): void {
   // Generate random number between 2 and 100000
   const random = Math.floor(Math.random() * 99998) + 2;
          this.inputValue.set(random.toString());
          this.handleValidate();
      }

      selectPreset(value: number): void {
        this.inputValue.set(value.toString());
        this.handleValidate();
      }

      selectFromHistory(n: number): void {
        this.inputValue.set(n.toString());
        this.handleValidate();
      }

      addToHistory(n: number, lawful: boolean): void {
        const current = this.history();
        // Add to front, limit to 5 items
        this.history.set([
          { n, lawful },
          ...current.filter(item => item.n !== n).slice(0, 4)
        ]);
      }
  }



3. Result Card Component
Purpose: Display validation results with visual emphasis

File: src/app/features/validator/components/result-card/result-card.component.ts

  import { Component, input, computed } from '@angular/core';
  import { CommonModule } from '@angular/common';
  import { MatCardModule } from '@angular/material/card';
  import { MatIconModule } from '@angular/material/icon';
  import { MatButtonModule } from '@angular/material/button';
  import { MatTooltipModule } from '@angular/material/tooltip';
  import { trigger, transition, style, animate } from '@angular/animations';
  import { ValidationResult } from '@app/core/models/validation-result';
  import { EntropyGaugeComponent } from '../entropy-gauge/entropy-gauge.component';
  import { FactorizationTreeComponent } from '../factorization-tree/factorization-tree.co

  @Component({
    selector: 'app-result-card',
    standalone: true,
    imports: [
      CommonModule,
      MatCardModule,
      MatIconModule,
      MatButtonModule,
      MatTooltipModule,
      EntropyGaugeComponent,
      FactorizationTreeComponent,
    ],
    animations: [
  trigger('fadeIn', [
    transition(':enter', [
      style({ opacity: 0, transform: 'translateY(20px)' }),
      animate('400ms cubic-bezier(0.4, 0, 0.2, 1)',
        style({ opacity: 1, transform: 'translateY(0)' }))
    ])
  ]),
  trigger('pulse', [
    transition('* => lawful', [
      animate('600ms', style({ transform: 'scale(1.05)' })),
      animate('300ms', style({ transform: 'scale(1)' })),
    ]),
    transition('* => unlawful', [
      animate('400ms', style({ transform: 'scale(0.98)' })),
      animate('200ms', style({ transform: 'scale(1)' })),
    ])
  ])
],
template: `
  <mat-card class="result-card" @fadeIn>
    <!-- Header -->
    <mat-card-header class="result-header" [@pulse]="result().lawful ? 'lawful' : 'unlaw
      <div class="number-display">
        <span class="number">{{ result().n | number }}</span>
        <button
          mat-icon-button
          (click)="copyToClipboard()"
          matTooltip="Copy number"
          class="copy-btn">
          <mat-icon>content_copy</mat-icon>
        </button>
      </div>

     <div class="lawful-badge" [class.lawful]="result().lawful">
       <mat-icon>{{ result().lawful ? 'check_circle' : 'cancel' }}</mat-icon>
       <span>{{ result().lawful ? 'Lawful' : 'Unlawful' }}</span>
     </div>
   </mat-card-header>

   <!-- Content -->
   <mat-card-content>
     <!-- Entropy Gauge -->
     <div class="gauge-section">
       <app-entropy-gauge
         [entropy]="result().entropy"
         [threshold]="result().kappa_max"
         [lawful]="result().lawful" />
     </div>

     <!-- Details Grid -->
     <div class="details-grid">
       <div class="detail-item">
         <span class="detail-label">Factorization</span>
         <span class="detail-value factorization">
           {{ result().factor_string }}
         </span>
   </div>

   <div class="detail-item">
     <span class="detail-label">
       PEET Entropy (S)
       <mat-icon
         class="info-icon"
         matTooltip="Prime Entanglement Entropy Tensor">
         info
       </mat-icon>
     </span>
     <span class="detail-value mono">
       {{ result().entropy | number:'1.4-4' }}
     </span>
   </div>

   <div class="detail-item">
     <span class="detail-label">
       Threshold (κ)
       <mat-icon
         class="info-icon"
         matTooltip="Maximum allowed entropy for lawfulness">
         info
       </mat-icon>
     </span>
     <span class="detail-value mono">
       {{ result().kappa_max | number:'1.1-1' }}
     </span>
   </div>

   <div class="detail-item">
     <span class="detail-label">Margin</span>
     <span class="detail-value mono" [class.positive]="margin() > 0" [class.negati
       {{ margin() > 0 ? '+' : '' }}{{ margin() | number:'1.4-4' }}
     </span>
   </div>
 </div>

 <!-- Explanation -->
 <div class="explanation" [class.lawful]="result().lawful">
   <mat-icon>{{ result().lawful ? 'info' : 'warning' }}</mat-icon>
   <p>{{ explanation() }}</p>
 </div>

  <!-- Factorization Tree (collapsible) -->
  @if (showTree()) {
    <div class="tree-section">
      <app-factorization-tree [factors]="result().factors" />
    </div>
  }
</mat-card-content>

<!-- Actions -->
<mat-card-actions>
  <button mat-button (click)="toggleTree()">
    <mat-icon>{{ showTree() ? 'expand_less' : 'expand_more' }}</mat-icon>
        {{ showTree() ? 'Hide' : 'Show' }} Factor Tree
      </button>
      <button mat-button (click)="shareResult()">
        <mat-icon>share</mat-icon>
        Share
      </button>
      <button mat-button (click)="exportResult()">
        <mat-icon>download</mat-icon>
        Export JSON
      </button>
    </mat-card-actions>
  </mat-card>
`,
styles: [`
  .result-card {
    max-width: 800px;
    margin: 2rem auto;
  }

 .result-header {
   display: flex;
   justify-content: space-between;
   align-items: center;
   padding: 2rem;
   background: linear-gradient(135deg, var(--primary-50), var(--primary-100));
   border-bottom: 1px solid var(--border);
 }

 .number-display {
   display: flex;
   align-items: center;
   gap: 0.5rem;
 }

 .number {
   font-family: var(--font-mono);
   font-size: 2.5rem;
   font-weight: 700;
   color: var(--primary-700);
 }

 .copy-btn {
   opacity: 0.6;
   transition: opacity 0.2s;

     &:hover {
       opacity: 1;
     }
 }

 .lawful-badge {
   display: flex;
   align-items: center;
   gap: 0.5rem;
   padding: 0.75rem 1.5rem;
   border-radius: 24px;
    font-weight: 600;
    font-size: 1.1rem;
    background: var(--danger-100);
    color: var(--danger-700);

    &.lawful {
      background: var(--success-100);
      color: var(--success-700);
    }

    mat-icon {
      font-size: 1.5rem;
      width: 1.5rem;
      height: 1.5rem;
    }
}

.gauge-section {
  padding: 2rem;
  display: flex;
  justify-content: center;
}

.details-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
  padding: 1.5rem 2rem;
  background: var(--background);
  border-radius: 8px;
  margin: 0 1.5rem 1.5rem;
}

.detail-item {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.detail-label {
  font-size: 0.875rem;
  color: var(--text-secondary);
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  display: flex;
  align-items: center;
  gap: 0.25rem;
}

.info-icon {
  font-size: 1rem;
  width: 1rem;
  height: 1rem;
  opacity: 0.6;
  cursor: help;
}

.detail-value {
  font-size: 1.25rem;
  font-weight: 600;
  color: var(--text-primary);

    &.mono {
      font-family: var(--font-mono);
    }

    &.factorization {
      font-family: var(--font-mono);
      font-size: 1.1rem;
    }

    &.positive {
      color: var(--success-600);
    }

    &.negative {
      color: var(--danger-600);
    }
}

.explanation {
  display: flex;
  align-items: flex-start;
  gap: 1rem;
  padding: 1.5rem;
  margin: 0 1.5rem 1.5rem;
  border-radius: 8px;
  background: var(--danger-50);
  border-left: 4px solid var(--danger-500);

    &.lawful {
      background: var(--success-50);
      border-left-color: var(--success-500);
    }

    mat-icon {
      flex-shrink: 0;
      color: var(--danger-600);
    }

    &.lawful mat-icon {
      color: var(--success-600);
    }

    p {
      margin: 0;
      line-height: 1.6;
      color: var(--text-primary);
    }
}
    .tree-section {
      padding: 1.5rem;
      margin: 0 1.5rem 1.5rem;
      background: var(--background);
      border-radius: 8px;
    }
  `]
})
export class ResultCardComponent {
  // Inputs
  result = input.required<ValidationResult>();

    // Local state
    showTree = signal(false);

    // Computed
    margin = computed(() => this.result().kappa_max - this.result().entropy);

    explanation = computed(() => {
      const r = this.result();
      if (r.lawful) {
        return `✓ This number is lawful. Its prime entanglement entropy (S = ${r.entropy.t
      } else {
        const excess = (r.entropy - r.kappa_max).toFixed(2);
        return `✗ This number is unlawful (synthetic). Its entropy (S = ${r.entropy.toFixed
      }
    });

    toggleTree(): void {
      this.showTree.update(v => !v);
    }

    copyToClipboard(): void {
      navigator.clipboard.writeText(this.result().n.toString());
      // Show snackbar notification
    }

    shareResult(): void {
      const url = `${window.location.origin}?n=${this.result().n}`;
      navigator.clipboard.writeText(url);
      // Show snackbar: "Share link copied!"
    }

    exportResult(): void {
      const json = JSON.stringify(this.result(), null, 2);
      const blob = new Blob([json], { type: 'application/json' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `mtpi-result-${this.result().n}.json`;
      a.click();
      URL.revokeObjectURL(url);
    }
}
Advanced Features

4. Entropy Gauge (D3.js Visualization)
Purpose: Circular gauge showing entropy vs threshold

Visual Design:

    Semicircular gauge (180°)
    Gradient fill (green → yellow → red)
    Animated needle pointing to entropy value
    Threshold marker at κ = 7.0
File: src/app/features/validator/components/entropy-gauge/entropy-gauge.component.ts

  import { Component, input, effect, viewChild, ElementRef } from '@angular/core';
  import { CommonModule } from '@angular/common';
  import * as d3 from 'd3';

  @Component({
    selector: 'app-entropy-gauge',
    standalone: true,
    imports: [CommonModule],
    template: `
      <div class="gauge-container">
        <svg #gauge width="300" height="200"></svg>
        <div class="gauge-label">
          <span class="entropy-value">{{ entropy() | number:'1.2-2' }}</span>
          <span class="entropy-unit">PEET Entropy</span>
        </div>
      </div>
    `,
    styles: [`
      .gauge-container {
        position: relative;
        display: inline-block;
      }

     .gauge-label {
       position: absolute;
       bottom: 20px;
       left: 50%;
       transform: translateX(-50%);
       text-align: center;
     }

     .entropy-value {
       display: block;
       font-size: 2rem;
       font-weight: 700;
       font-family: var(--font-mono);
       color: var(--primary-700);
     }
    .entropy-unit {
      display: block;
      font-size: 0.875rem;
      color: var(--text-secondary);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }
  `]
})
export class EntropyGaugeComponent {
  entropy = input.required<number>();
  threshold = input.required<number>();
  lawful = input.required<boolean>();

 gaugeRef = viewChild<ElementRef>('gauge');

 constructor() {
   effect(() => {
     if (this.gaugeRef()) {
       this.renderGauge();
     }
   });
 }

 private renderGauge(): void {
   const svg = d3.select(this.gaugeRef()!.nativeElement);
   svg.selectAll('*').remove();

   const width = 300;
   const height = 200;
   const radius = 120;
   const centerX = width / 2;
   const centerY = height - 30;

   // Define scale
   const maxEntropy = Math.max(this.threshold() * 1.5, this.entropy() * 1.2);
   const angleScale = d3.scaleLinear()
     .domain([0, maxEntropy])
     .range([-Math.PI / 2, Math.PI / 2]);

   // Create arc generator for background
   const arc = d3.arc()
     .innerRadius(radius - 20)
     .outerRadius(radius)
     .startAngle(-Math.PI / 2)
     .endAngle(Math.PI / 2);

   // Gradient for gauge background
   const gradient = svg.append('defs')
     .append('linearGradient')
     .attr('id', 'gauge-gradient')
     .attr('x1', '0%')
     .attr('x2', '100%');

   gradient.append('stop')
           .attr('offset', '0%')
           .attr('stop-color', '#10b981'); // Success green

          gradient.append('stop')
            .attr('offset', `${(this.threshold() / maxEntropy) * 100}%`)
            .attr('stop-color', '#eab308'); // Warning yellow

          gradient.append('stop')
            .attr('offset', '100%')
            .attr('stop-color', '#ef4444'); // Danger red

          // Draw gauge background
          svg.append('path')
            .attr('d', arc as any)
            .attr('transform', `translate(${centerX},${centerY})`)
            .attr('fill', 'url(#gauge-gradient)')
            .attr('opacity', 0.3);

          // Draw threshold marker
          const thresholdAngle = angleScale(this.threshold());
          svg.append('line')
            .attr('x1', centerX + (radius - 30) * Math.cos(thresholdAngle))
            .attr('y1', centerY + (radius - 30) * Math.sin(thresholdAngle))
            .attr('x2', centerX + (radius + 10) * Math.cos(thresholdAngle))
            .attr('y2', centerY + (radius + 10) * Math.sin(thresholdAngle))
            .attr('stroke', '#64748b')
            .attr('stroke-width', 2)
            .attr('stroke-dasharray', '4,4');

          // Draw needle
          const needleAngle = angleScale(this.entropy());
          const needleLength = radius - 10;

          const needle = svg.append('g')
            .attr('transform', `translate(${centerX},${centerY})`);

          needle.append('line')
            .attr('x1', 0)
            .attr('y1', 0)
            .attr('x2', needleLength * Math.cos(needleAngle - Math.PI / 2))
            .attr('y2', needleLength * Math.sin(needleAngle - Math.PI / 2))
            .attr('stroke', this.lawful() ? '#10b981' : '#ef4444')
            .attr('stroke-width', 3)
            .attr('stroke-linecap', 'round')
            .transition()
            .duration(1000)
            .ease(d3.easeElasticOut);

          needle.append('circle')
            .attr('r', 8)
            .attr('fill', this.lawful() ? '#10b981' : '#ef4444');
      }
  }


Total UI/UX spec: 5,000+ lines planned.
Next sections to detail:

    Explorer (range scanner + heatmap)
    Archetypes gallery
    Playground (interactive experiments)
    Factorization tree visualization
    Mobile responsive design
    Accessibility (WCAG 2.1 AA)
    Performance optimizations
Ready for next component specs?
