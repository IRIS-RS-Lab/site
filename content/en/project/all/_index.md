---
title: ''
linkTitle: Project List
weight: 10
type: landing
sections:
  - block: markdown
    content:
      title: ''
      text: |
        {{< section_nav >}}
  - block: collection
    id: projects_all
    content:
      title: Project List
      subtitle: ''
      count: 0
      filters:
        folders:
          - project
        tag: ""
        category: ""
        featured_only: false
        exclude_featured: false
        exclude_future: false
        exclude_past: false
      offset: 0
      sort_by: "Date"
      sort_ascending: false
    design:
      view: card
---
