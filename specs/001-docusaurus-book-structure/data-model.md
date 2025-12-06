# Data Model: Docusaurus Book Structure

**Feature**: [specs/1-docusaurus-book-structure/spec.md](specs/1-docusaurus-book-structure/spec.md)
**Plan**: [specs/1-docusaurus-book-structure/plan.md](specs/1-docusaurus-book-structure/plan.md)
**Date**: 2025-12-04

## Entities

### Chapter
- **Description**: A primary section of the book, containing detailed content on a specific topic.
- **Attributes**:
    - `title`: (string) The title of the chapter.
    - `content`: (string) The main body of the chapter, in Markdown format.
    - `word_count`: (integer) The number of words in the chapter (between 600 and 1,200, as per FR-002).
    - `diagrams`: (list of Diagram entities) Embedded Mermaid diagram definitions.
    - `citations`: (list of Citation entities) APA-formatted citations.
    - `tutorials`: (list of Tutorial entities) Associated tutorials within the chapter.
- **Relationships**: Contains multiple Tutorials, Diagrams, and Citations.

### Tutorial
- **Description**: A guided instructional section embedded within a Chapter, detailing practical steps for a technology.
- **Attributes**:
    - `title`: (string) The title of the tutorial.
    - `content`: (string) Step-by-step instructions and code examples.
    - `technologies_covered`: (list of strings) e.g., "ROS 2", "Gazebo", "Isaac", "VLA" (as per FR-005).
- **Relationships**: Belongs to a Chapter.

### Diagram
- **Description**: A visual representation embedded in a Chapter, defined using Mermaid syntax.
- **Attributes**:
    - `mermaid_syntax`: (string) The Mermaid diagram definition.
    - `caption`: (string, optional) A brief description of the diagram.
- **Relationships**: Belongs to a Chapter.

### Citation
- **Description**: A reference to a source within a Chapter, formatted according to APA style.
- **Attributes**:
    - `text`: (string) The full APA-formatted citation text.
    - `source_url`: (string, optional) URL to the source if available.
- **Relationships**: Belongs to a Chapter.

### Weekly Breakdown
- **Description**: An appendix section providing an overview of weekly progress for the project.
- **Attributes**:
    - `content`: (string) Markdown content detailing weekly progress, tasks, and achievements.
- **Relationships**: N/A (standalone appendix).
