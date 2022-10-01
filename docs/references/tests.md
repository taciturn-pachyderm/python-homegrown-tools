---
template: reference.html
---
# Tests Reference

::: tests
    options:
      setup_commands:
        - import sys
        - sys.path.append('..')
      paths:
        - ..
      merge_init_into_class: true
      members_order: alphabetical
      show_submodules: true  # recursively include all module objects
      show_root_heading: false
      show_root_toc_entry: false
      show_root_full_path: true
      show_root_members_full_path: true
      show_object_full_path: false
      show_category_heading: false
      show_if_no_docstring: true
      show_signature_annotations: true
      show_signature: true
      separate_signature: false