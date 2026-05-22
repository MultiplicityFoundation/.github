---
slug: wordpress-themes-plugins
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 03-case-studies/Wordpress Themes Plugins.md
  last_synced: '2026-03-20T17:17:20.450092Z'
---

The “lawfulness-first” playbook for building WordPress themes and plugins that are ethical,
secure, and monetizable—aligned with the Maxims of Multiplicity (lawfulness, provenance,
sovereignty, reversibility).



Foundation (applies to both)
1) Licensing & attribution (Lawfulness First)

   ●​ Use GPL‑compatible licenses for all code you ship. Declare SPDX headers in every file
      and full license in root.​

   ●​ Attribute third‑party assets (fonts, images, models) with their specific licenses; bundle
      only if permitted.​

   ●​ No obfuscated code, no remote, auto‑executed PHP/JS from unknown domains.​


2) Consent, data minimization, and transparency (Sovereignty by Design)

   ●​ Collect only what you need; default to opt‑in for telemetry/analytics.​

   ●​ Provide a human‑readable Privacy panel explaining: what you collect, why, where it
      goes, retention, and how to delete.​

   ●​ Implement a “data export & erase” action integrated with WordPress’ personal data
      tools.​


3) Security & integrity (Redundancy Builds Trust)

   ●​ Never trust input. Validate → Sanitize → Escape. Enforce capability checks.​

   ●​ Use nonces for all state‑changing actions.​

   ●​ Sign updates; verify package integrity; pin dependency versions; include a minimal
      SBOM (package-lock.json/composer.lock + a SBOM file).​


4) Accessibility & internationalization (Clarity over Control)

   ●​ WCAG 2.1 AA: keyboard focus, color contrast, ARIA where needed.​
   ●​ Make it translatable (i18n): __(), _e(), esc_html__(), text domain, .pot file.​

   ●​ RTL styles where applicable.​


5) Performance & reversibility (Coherence before Scale)

   ●​ Lazy‑load heavy assets, enqueue only where needed, and provide a “safe mode”
      (disable features if errors).​

   ●​ Provide uninstall cleaners and rollback points (remove options/transients if user
      consents).​




Plugin lawfulness checklist (+ secure patterns)
Headers

php
CopyEdit
<?php
/**
 * Plugin Name: Example Plugin
 * Description: …
 * Version: 1.0.0
 * Author: …
 * License: GPL-2.0-or-later
 * Text Domain: example-plugin
 */
if (!defined('ABSPATH')) exit;


Capabilities, nonces, sanitization

php
CopyEdit
// Admin action with nonce + capability
add_action('admin_post_example_save', function () {
  if (!current_user_can('manage_options')) wp_die('Forbidden', 403);
    if (!isset($_POST['_wpnonce']) ||
!wp_verify_nonce($_POST['_wpnonce'], 'example_save')) wp_die('CSRF',
403);


    $title = sanitize_text_field($_POST['title'] ?? '');
    update_option('example_title', $title); // Prefer a namespaced
option key
    wp_safe_redirect(admin_url('options-general.php?page=example'));
    exit;
});


REST API route with permission callback

php
CopyEdit
add_action('rest_api_init', function () {
    register_rest_route('example/v1', '/items', [
      'methods'      => 'POST',
      'callback' => 'example_create_item',
      'permission_callback' => function () {
          return current_user_can('edit_posts'); // Fine-grained caps
      },
      'args' => [
          'name' =>
['type'=>'string','required'=>true,'sanitize_callback'=>'sanitize_text
_field'],
      ],
    ]);
});


function example_create_item(WP_REST_Request $req) {
    $name = $req->get_param('name'); // sanitized via args
    // … create item
    return new WP_REST_Response(['ok'=>true], 201);
}


Escaping in output
php
CopyEdit
echo '<h2>' . esc_html(get_option('example_title', '')) . '</h2>';
echo wp_kses_post($trusted_html_fragment);


Enqueue scripts/styles correctly

php
CopyEdit
add_action('admin_enqueue_scripts', function($hook){
    if ($hook !== 'settings_page_example') return;
    wp_enqueue_script('example-admin', plugins_url('assets/admin.js',
__FILE__), ['wp-element'], '1.0.0', true);
    wp_enqueue_style('example-admin', plugins_url('assets/admin.css',
__FILE__), [], '1.0.0');
});


Uninstall cleanup (opt‑in)

php
CopyEdit
// uninstall.php (standalone file)
if (!defined('WP_UNINSTALL_PLUGIN')) exit;
$preserve = get_option('example_preserve_data', false);
if (!$preserve) {
    delete_option('example_title');
    // delete custom tables/transients as needed
}


Monetization ethics

    ●​ Gate premium features via capabilities keyed to a license check; never break basic site
       functionality if the license lapses.​

    ●​ Fail closed for network calls (timeouts, retries) and provide a “local only” mode.​

    ●​ Disclose any external API calls and their data shape.​
Theme lawfulness checklist (+ secure patterns)
Headers

css
CopyEdit
/*
Theme Name: Example Theme
Author: …
Version: 1.0.0
License: GPL-2.0-or-later
Text Domain: example-theme
*/


Block theme best practices

     ●​ Use theme.json for design tokens (colors, spacing, typography).​

     ●​ Don’t bundle page builder lock‑ins; stick to core blocks or well‑documented patterns.​

     ●​ Template hierarchy with minimal PHP; keep logic in plugins, not themes.​


Enqueue only what’s needed

php
CopyEdit
add_action('wp_enqueue_scripts', function () {
  wp_enqueue_style('example-style', get_stylesheet_uri(), [],
wp_get_theme()->get('Version'));
  if (is_singular()) wp_enqueue_script('comment-reply');
});


No data collection in themes

     ●​ A theme should not phone home or collect analytics. If you must, move that to a plugin,
        disclose, and make it opt‑in.​


Accessibility
   ●​ Proper document outline, skip links, focus styles, landmark roles, and accessible nav
      toggles.​




Data, privacy, and CSL guardrails (QARI‑aligned)
CSL policy document (ship it in your plugin/theme)

   ●​ Define unacceptable content (harassment, hate, PII exfiltration) and how your UI
      prevents/flags it.​

   ●​ Provide a consent switch for any automated analysis (e.g., “Index content for
      recommendations”).​

   ●​ Record provenance: version, user, timestamp for any transformation (supports rollback
      & audits).​


Telemetry contract

   ●​ Schema: { event, user_capability_level, coarse_timestamp, no PII }​

   ●​ Storage: local first, opt‑in remote. Offer data erasure and export.​




Code quality gates
   ●​ Static analysis: PHP_CodeSniffer with WordPress Coding Standards; ESLint for JS;
      Prettier for formatting.​

   ●​ Dependency hygiene: use Composer/npm locks, avoid requireing remote files, and
      validate checksums for updates.​

   ●​ Automated tests: WP‑CLI scaffold + PHPUnit for PHP; Playwright or Jest for blocks.​

   ●​ SBOM: include a generated CycloneDX or SPDX file on release builds.​
Distribution & updates
   ●​ Readme discipline: clear change logs, breaking change notes, minimum WP/PHP
      versions.​

   ●​ Auto‑updates: support WordPress’ update system; sign zips if you run your own
      updater.​

   ●​ Rollback: ship a one‑click rollback to the previous stable (store last version URL; verify
      checksum).​




Common violations to avoid (Do‑Not list)
   ●​ Storing plaintext secrets or tokens in options.​

   ●​ Running eval/Function on untrusted input; dynamic includes from URLs.​

   ●​ Disabling core security headers or privacy tools.​

   ●​ Hijacking admin notices with persistent nags; degrading UX on license expiry.​

   ●​ Bundling premium code under non‑GPL while claiming GPL compatibility.​




Minimal lawful templates
Consent toggle (settings)

php
CopyEdit
add_settings_field('example_index_optin', __('Index my content',
'example-plugin'), function(){
  $v = (bool) get_option('example_index_optin', false);
  echo '<label><input type="checkbox" name="example_index_optin"
value="1" '.checked($v, true, false).'/> ' . esc_html__('Allow
semantic indexing for recommendations.', 'example-plugin') .
'</label>';
}, 'reading', 'default');
register_setting('reading', 'example_index_optin', ['type'=>'boolean',
'sanitize_callback'=>'rest_sanitize_boolean']);


Capability map (roles)

php
CopyEdit
register_activation_hook(__FILE__, function(){
  $role = get_role('administrator');
  if ($role && !$role->has_cap('example_manage'))
$role->add_cap('example_manage');
});


GDPR/CCPA helpers

   ●​ Add “Export/Erase” handlers that remove your plugin’s options/tables for a user.​

   ●​ Document data flows in your readme and plugin Settings → Privacy tab.​




Quick compliance checklist (print this)
   ●​ GPL‑compatible license declared (code + assets)​

   ●​ No obfuscation; no remote executable code​

   ●​ Cap checks + nonces on every state change​

   ●​ Validate → Sanitize → Escape everywhere​

   ●​ i18n ready; .pot provided​

   ●​ Accessibility tested (keyboard/contrast)​

   ●​ Privacy page & opt‑in for analytics/indexing​

   ●​ Data export/erase supported​
●​ Uninstall cleanup (user‑controlled)​

●​ SBOM + locked dependencies​

●​ Clear changelog and rollback path​
