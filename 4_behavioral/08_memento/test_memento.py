"""
Testy dla Memento Pattern - Workflow Snapshots
"""

import pytest
from datetime import datetime, timedelta
from starter import (
    DocumentMemento, ProjectMemento,
    DocumentOriginator, ProjectOriginator,
    SnapshotContainer, WorkflowCaretaker,
    demonstrate_workflow_snapshots
)


class TestDocumentMemento:
    """Testy DocumentMemento"""

    def test_document_memento_creation(self):
        """Test tworzenia document memento"""
        metadata = {"author": "John", "category": "spec"}
        memento = DocumentMemento("Test Doc", "Content", metadata, 1)

        assert memento.get_title() == "Test Doc"
        assert memento.get_content() == "Content"
        assert memento.get_version() == 1
        assert isinstance(memento.get_timestamp(), datetime)

    def test_document_memento_metadata_immutability(self):
        """Test immutability metadanych w memento"""
        original_metadata = {"author": "John", "tags": ["spec", "draft"]}
        memento = DocumentMemento("Test", "Content", original_metadata, 1)

        # Modyfikacja oryginalnych metadanych nie powinna wpłynąć na memento
        original_metadata["author"] = "Jane"
        original_metadata["tags"].append("final")

        retrieved_metadata = memento.get_metadata()
        assert retrieved_metadata["author"] == "John"
        assert "final" not in retrieved_metadata["tags"]

    def test_document_memento_metadata_copy(self):
        """Test że get_metadata zwraca kopię"""
        metadata = {"author": "John", "tags": []}
        memento = DocumentMemento("Test", "Content", metadata, 1)

        # Modyfikacja zwróconej kopii nie powinna wpłynąć na memento
        retrieved_metadata = memento.get_metadata()
        retrieved_metadata["author"] = "Modified"
        retrieved_metadata["tags"].append("new_tag")

        fresh_metadata = memento.get_metadata()
        assert fresh_metadata["author"] == "John"
        assert len(fresh_metadata["tags"]) == 0

    def test_document_memento_timestamp(self):
        """Test timestamp w memento"""
        before = datetime.now()
        memento = DocumentMemento("Test", "Content", {}, 1)
        after = datetime.now()

        assert before <= memento.get_timestamp() <= after


class TestProjectMemento:
    """Testy ProjectMemento"""

    def test_project_memento_creation(self):
        """Test tworzenia project memento"""
        documents = {
            "README": {"content": "Project description", "version": 1},
            "SPEC": {"content": "Specifications", "version": 2}
        }
        settings = {"theme": "dark", "auto_save": True}

        memento = ProjectMemento("TestProject", documents, "Active", settings)

        assert memento.get_name() == "TestProject"
        assert memento.get_status() == "Active"
        assert len(memento.get_documents()) == 2
        assert memento.get_settings()["theme"] == "dark"

    def test_project_memento_deep_copy(self):
        """Test deep copy w project memento"""
        documents = {
            "README": {"content": "Original", "tags": ["important"]}
        }
        settings = {"features": ["feature1"]}

        memento = ProjectMemento("Test", documents, "Active", settings)

        # Modyfikacja oryginalnych struktur
        documents["README"]["content"] = "Modified"
        documents["README"]["tags"].append("changed")
        settings["features"].append("feature2")

        # Memento powinno zachować oryginalne wartości
        retrieved_docs = memento.get_documents()
        retrieved_settings = memento.get_settings()

        assert retrieved_docs["README"]["content"] == "Original"
        assert "changed" not in retrieved_docs["README"]["tags"]
        assert "feature2" not in retrieved_settings["features"]


class TestDocumentOriginator:
    """Testy DocumentOriginator"""

    def test_document_originator_creation(self):
        """Test tworzenia document originator"""
        doc = DocumentOriginator("My Document")

        assert doc.title == "My Document"
        assert doc.content == ""
        assert doc.version == 1
        assert isinstance(doc.last_modified, datetime)

    def test_document_originator_edit(self):
        """Test edycji dokumentu"""
        doc = DocumentOriginator("Test Doc")
        original_version = doc.version
        original_modified = doc.last_modified

        doc.edit("New content")

        assert doc.content == "New content"
        assert doc.version == original_version + 1
        assert doc.last_modified > original_modified

    def test_document_originator_metadata(self):
        """Test aktualizacji metadanych"""
        doc = DocumentOriginator("Test Doc")

        doc.update_metadata("author", "John Doe")
        doc.update_metadata("category", "specification")

        assert doc.metadata["author"] == "John Doe"
        assert doc.metadata["category"] == "specification"

    def test_document_originator_create_memento(self):
        """Test tworzenia memento"""
        doc = DocumentOriginator("Test Doc")
        doc.edit("Some content")
        doc.update_metadata("author", "John")

        memento = doc.create_memento()

        assert memento.get_title() == "Test Doc"
        assert memento.get_content() == "Some content"
        assert memento.get_metadata()["author"] == "John"
        assert memento.get_version() == doc.version

    def test_document_originator_restore_from_memento(self):
        """Test przywracania stanu z memento"""
        doc = DocumentOriginator("Original Title")
        doc.edit("Original content")
        doc.update_metadata("status", "draft")

        # Stwórz memento
        memento = doc.create_memento()

        # Zmień stan dokumentu
        doc.edit("Modified content")
        doc.update_metadata("status", "final")
        doc.update_metadata("author", "Jane")

        # Przywróć z memento
        doc.restore_from_memento(memento)

        assert doc.title == "Original Title"
        assert doc.content == "Original content"
        assert doc.metadata["status"] == "draft"
        assert "author" not in doc.metadata

    def test_document_originator_state_summary(self):
        """Test podsumowania stanu"""
        doc = DocumentOriginator("Test")
        doc.edit("Some content here")

        summary = doc.get_state_summary()

        assert summary["title"] == "Test"
        assert summary["content_length"] == len("Some content here")
        assert summary["version"] == doc.version
        assert "last_modified" in summary


class TestProjectOriginator:
    """Testy ProjectOriginator"""

    def test_project_originator_creation(self):
        """Test tworzenia project originator"""
        project = ProjectOriginator("WebApp")

        assert project.name == "WebApp"
        assert len(project.documents) == 0
        assert project.status == "New"
        assert "theme" in project.settings

    def test_project_originator_add_document(self):
        """Test dodawania dokumentu do projektu"""
        project = ProjectOriginator("WebApp")

        project.add_document("README", "Project description")

        assert "README" in project.documents
        assert project.documents["README"]["content"] == "Project description"
        assert project.documents["README"]["version"] == 1

    def test_project_originator_update_document(self):
        """Test aktualizacji dokumentu w projekcie"""
        project = ProjectOriginator("WebApp")
        project.add_document("README", "Original content")

        original_version = project.documents["README"]["version"]
        project.update_document("README", "Updated content")

        assert project.documents["README"]["content"] == "Updated content"
        assert project.documents["README"]["version"] == original_version + 1

    def test_project_originator_remove_document(self):
        """Test usuwania dokumentu z projektu"""
        project = ProjectOriginator("WebApp")
        project.add_document("README", "Content")
        project.add_document("SPEC", "Specifications")

        project.remove_document("README")

        assert "README" not in project.documents
        assert "SPEC" in project.documents

    def test_project_originator_set_status(self):
        """Test ustawiania statusu projektu"""
        project = ProjectOriginator("WebApp")

        project.set_status("In Progress")

        assert project.status == "In Progress"

    def test_project_originator_update_setting(self):
        """Test aktualizacji ustawień projektu"""
        project = ProjectOriginator("WebApp")

        project.update_setting("theme", "dark")
        project.update_setting("auto_backup", False)

        assert project.settings["theme"] == "dark"
        assert project.settings["auto_backup"] is False

    def test_project_originator_create_memento(self):
        """Test tworzenia memento projektu"""
        project = ProjectOriginator("WebApp")
        project.add_document("README", "Description")
        project.set_status("Active")
        project.update_setting("theme", "dark")

        memento = project.create_memento()

        assert memento.get_name() == "WebApp"
        assert memento.get_status() == "Active"
        assert "README" in memento.get_documents()
        assert memento.get_settings()["theme"] == "dark"

    def test_project_originator_restore_from_memento(self):
        """Test przywracania stanu projektu z memento"""
        project = ProjectOriginator("WebApp")
        project.add_document("README", "Original")
        project.set_status("Draft")

        # Stwórz memento
        memento = project.create_memento()

        # Zmień stan
        project.add_document("SPEC", "New spec")
        project.update_document("README", "Modified")
        project.set_status("Active")

        # Przywróć z memento
        project.restore_from_memento(memento)

        assert project.status == "Draft"
        assert project.documents["README"]["content"] == "Original"
        assert "SPEC" not in project.documents

    def test_project_originator_summary(self):
        """Test podsumowania projektu"""
        project = ProjectOriginator("WebApp")
        project.add_document("README", "Description")
        project.add_document("SPEC", "Specifications")

        summary = project.get_project_summary()

        assert summary["name"] == "WebApp"
        assert summary["document_count"] == 2
        assert summary["status"] == "New"
        assert "last_modified" in summary


class TestSnapshotContainer:
    """Testy SnapshotContainer"""

    def test_snapshot_container_creation(self):
        """Test tworzenia snapshot container"""
        doc = DocumentOriginator("Test")
        memento = doc.create_memento()

        container = SnapshotContainer(memento, "Initial version", ["draft", "v1"])

        assert container.description == "Initial version"
        assert "draft" in container.tags
        assert "v1" in container.tags
        assert container.snapshot_id.startswith("SNAP_")

    def test_snapshot_container_has_tag(self):
        """Test sprawdzania tagów"""
        container = SnapshotContainer(None, "Test", ["important", "review"])

        assert container.has_tag("important") is True
        assert container.has_tag("review") is True
        assert container.has_tag("draft") is False

    def test_snapshot_container_matches_description(self):
        """Test wyszukiwania w opisie"""
        container = SnapshotContainer(None, "Initial version for review", [])

        assert container.matches_description("initial") is True
        assert container.matches_description("VERSION") is True
        assert container.matches_description("review") is True
        assert container.matches_description("final") is False


class TestWorkflowCaretaker:
    """Testy WorkflowCaretaker"""

    def test_workflow_caretaker_creation(self):
        """Test tworzenia workflow caretaker"""
        caretaker = WorkflowCaretaker()

        assert len(caretaker.snapshots) == 0
        assert len(caretaker.project_snapshots) == 0
        assert len(caretaker.named_snapshots) == 0
        assert caretaker.auto_save_enabled is True

    def test_caretaker_save_snapshot(self):
        """Test zapisywania snapshot dokumentu"""
        caretaker = WorkflowCaretaker()
        doc = DocumentOriginator("Test Doc")
        doc.edit("Some content")

        snapshot_id = caretaker.save_snapshot(doc, "Initial version")

        assert len(caretaker.snapshots) == 1
        assert snapshot_id.startswith("SNAP_")
        assert caretaker.snapshots[0].description == "Initial version"

    def test_caretaker_save_project_snapshot(self):
        """Test zapisywania snapshot projektu"""
        caretaker = WorkflowCaretaker()
        project = ProjectOriginator("WebApp")
        project.add_document("README", "Description")

        snapshot_id = caretaker.save_project_snapshot(project, "Project setup")

        assert len(caretaker.project_snapshots) == 1
        assert snapshot_id.startswith("SNAP_")

    def test_caretaker_restore_snapshot(self):
        """Test przywracania snapshot dokumentu"""
        caretaker = WorkflowCaretaker()
        doc = DocumentOriginator("Test Doc")

        # Stan początkowy
        doc.edit("Original content")
        caretaker.save_snapshot(doc, "Original version")

        # Zmień stan
        doc.edit("Modified content")
        assert doc.content == "Modified content"

        # Przywróć
        success = caretaker.restore_snapshot(doc, "Original version")

        assert success is True
        assert doc.content == "Original content"

    def test_caretaker_restore_nonexistent_snapshot(self):
        """Test przywracania nieistniejącego snapshot"""
        caretaker = WorkflowCaretaker()
        doc = DocumentOriginator("Test Doc")

        success = caretaker.restore_snapshot(doc, "Nonexistent")

        assert success is False

    def test_caretaker_create_milestone(self):
        """Test tworzenia milestone"""
        caretaker = WorkflowCaretaker()
        doc = DocumentOriginator("Test Doc")
        doc.edit("Final content")

        snapshot_id = caretaker.create_milestone(doc, "Release v1.0", ["release", "stable"])

        assert "Release v1.0" in caretaker.named_snapshots
        assert caretaker.named_snapshots["Release v1.0"].has_tag("release")
        assert snapshot_id.startswith("SNAP_")

    def test_caretaker_restore_milestone(self):
        """Test przywracania milestone"""
        caretaker = WorkflowCaretaker()
        doc = DocumentOriginator("Test Doc")

        # Stwórz milestone
        doc.edit("Milestone content")
        caretaker.create_milestone(doc, "Important Milestone")

        # Zmień stan
        doc.edit("Changed content")

        # Przywróć milestone
        success = caretaker.restore_milestone(doc, "Important Milestone")

        assert success is True
        assert doc.content == "Milestone content"

    def test_caretaker_get_milestone(self):
        """Test pobierania milestone"""
        caretaker = WorkflowCaretaker()
        doc = DocumentOriginator("Test Doc")

        caretaker.create_milestone(doc, "Test Milestone", ["test"])

        milestone = caretaker.get_milestone("Test Milestone")

        assert milestone is not None
        assert milestone.has_tag("test")

        nonexistent = caretaker.get_milestone("Nonexistent")
        assert nonexistent is None

    def test_caretaker_list_snapshots_by_tag(self):
        """Test listowania snapshots po tagu"""
        caretaker = WorkflowCaretaker()
        doc = DocumentOriginator("Test Doc")

        # Stwórz snapshots z różnymi tagami
        caretaker.create_milestone(doc, "Release 1", ["release", "stable"])
        caretaker.create_milestone(doc, "Release 2", ["release", "beta"])
        caretaker.create_milestone(doc, "Backup", ["backup"])

        release_snapshots = caretaker.list_snapshots_by_tag("release")
        stable_snapshots = caretaker.list_snapshots_by_tag("stable")
        backup_snapshots = caretaker.list_snapshots_by_tag("backup")

        assert len(release_snapshots) == 2
        assert len(stable_snapshots) == 1
        assert len(backup_snapshots) == 1

    def test_caretaker_cleanup_old_snapshots(self):
        """Test czyszczenia starych snapshots"""
        caretaker = WorkflowCaretaker()
        doc = DocumentOriginator("Test Doc")

        # Symuluj stare snapshots (nie można łatwo zmienić timestamp, więc test podstawowy)
        caretaker.save_snapshot(doc, "Recent snapshot")
        caretaker.create_milestone(doc, "Important", ["keep"])  # Milestones nie powinny być usuwane

        # Test cleanup (może nie usunąć nic z powodu timestamp)
        removed_count = caretaker.cleanup_old_snapshots(1)

        # Milestones powinny zostać nietknięte
        assert "Important" in caretaker.named_snapshots

    def test_caretaker_get_statistics(self):
        """Test statystyk caretaker"""
        caretaker = WorkflowCaretaker()
        doc = DocumentOriginator("Test Doc")
        project = ProjectOriginator("Test Project")

        # Dodaj różne snapshots
        caretaker.save_snapshot(doc, "Doc snapshot 1")
        caretaker.save_snapshot(doc, "Doc snapshot 2")
        caretaker.save_project_snapshot(project, "Project snapshot")
        caretaker.create_milestone(doc, "Milestone 1")

        stats = caretaker.get_caretaker_statistics()

        assert stats["total_snapshots"] == 2
        assert stats["total_project_snapshots"] == 1
        assert stats["named_snapshots"] == 1
        assert "oldest_snapshot" in stats
        assert "newest_snapshot" in stats


class TestMementoPattern:
    """Testy wzorca Memento w kompleksowych scenariuszach"""

    def test_document_versioning_workflow(self):
        """Test workflow wersjonowania dokumentu"""
        caretaker = WorkflowCaretaker()
        doc = DocumentOriginator("Requirements Document")

        # Workflow: draft -> review -> final
        doc.edit("Initial requirements draft")
        caretaker.save_snapshot(doc, "Draft version")

        doc.edit("Requirements with stakeholder feedback")
        caretaker.save_snapshot(doc, "Review version")

        doc.edit("Final requirements specification")
        caretaker.create_milestone(doc, "Final v1.0", ["final", "v1.0"])

        # Przypadkowa zmiana
        doc.edit("Accidentally deleted content")

        # Przywróć do final version
        success = caretaker.restore_milestone(doc, "Final v1.0")

        assert success is True
        assert doc.content == "Final requirements specification"

    def test_project_backup_and_restore(self):
        """Test backup i restore całego projektu"""
        caretaker = WorkflowCaretaker()
        project = ProjectOriginator("E-commerce Platform")

        # Setup początkowy projektu
        project.add_document("README", "E-commerce platform description")
        project.add_document("API_SPEC", "REST API specifications")
        project.set_status("Development")
        project.update_setting("environment", "staging")

        # Backup przed dużymi zmianami
        caretaker.save_project_snapshot(project, "Before major refactoring")

        # Duże zmiany
        project.remove_document("API_SPEC")
        project.add_document("GRAPHQL_SPEC", "GraphQL API specifications")
        project.set_status("Refactoring")
        project.update_setting("environment", "development")

        # Zmiany nie działają, przywróć backup
        success = caretaker.restore_project_snapshot(project, "Before major refactoring")

        assert success is True
        assert "API_SPEC" in project.documents
        assert "GRAPHQL_SPEC" not in project.documents
        assert project.status == "Development"
        assert project.settings["environment"] == "staging"

    def test_multiple_snapshots_management(self):
        """Test zarządzania wieloma snapshots"""
        caretaker = WorkflowCaretaker()

        # Różne dokumenty
        doc1 = DocumentOriginator("User Guide")
        doc2 = DocumentOriginator("Technical Spec")

        # Różne projekty
        project1 = ProjectOriginator("Frontend")
        project2 = ProjectOriginator("Backend")

        # Stwórz snapshots
        doc1.edit("User guide content")
        caretaker.save_snapshot(doc1, "User guide v1")

        doc2.edit("Technical specifications")
        caretaker.create_milestone(doc2, "Tech Spec Milestone", ["technical"])

        project1.add_document("README", "Frontend project")
        caretaker.save_project_snapshot(project1, "Frontend initial")

        project2.add_document("API", "Backend API")
        caretaker.save_project_snapshot(project2, "Backend initial")

        # Sprawdź statystyki
        stats = caretaker.get_caretaker_statistics()
        assert stats["total_snapshots"] == 1  # Tylko doc1 snapshot
        assert stats["total_project_snapshots"] == 2
        assert stats["named_snapshots"] == 1  # Milestone dla doc2

    def test_snapshot_isolation(self):
        """Test izolacji snapshots"""
        caretaker = WorkflowCaretaker()
        doc = DocumentOriginator("Shared Document")

        # Stwórz snapshot
        doc.edit("Original content")
        doc.update_metadata("author", "John")
        caretaker.save_snapshot(doc, "Original state")

        # Zmień dokument
        doc.edit("Modified content")
        doc.update_metadata("author", "Jane")
        doc.update_metadata("reviewer", "Bob")

        # Stwórz drugi snapshot
        caretaker.save_snapshot(doc, "Modified state")

        # Przywróć pierwszy snapshot
        caretaker.restore_snapshot(doc, "Original state")

        # Sprawdź że zmiany z drugiego snapshot nie wpłynęły na pierwszy
        assert doc.content == "Original content"
        assert doc.metadata["author"] == "John"
        assert "reviewer" not in doc.metadata

    def test_milestone_tagging_and_search(self):
        """Test tagowania i wyszukiwania milestones"""
        caretaker = WorkflowCaretaker()
        doc = DocumentOriginator("Release Notes")

        # Stwórz milestones z różnymi tagami
        doc.edit("Alpha release notes")
        caretaker.create_milestone(doc, "Alpha Release", ["alpha", "testing"])

        doc.edit("Beta release notes")
        caretaker.create_milestone(doc, "Beta Release", ["beta", "testing"])

        doc.edit("Final release notes")
        caretaker.create_milestone(doc, "Production Release", ["production", "stable"])

        # Wyszukaj po tagach
        testing_snapshots = caretaker.list_snapshots_by_tag("testing")
        stable_snapshots = caretaker.list_snapshots_by_tag("stable")

        assert len(testing_snapshots) == 2
        assert len(stable_snapshots) == 1

        # Sprawdź konkretne milestones
        alpha = caretaker.get_milestone("Alpha Release")
        assert alpha.has_tag("alpha")
        assert alpha.has_tag("testing")

    def test_memento_immutability_enforcement(self):
        """Test wymuszania immutability w memento"""
        doc = DocumentOriginator("Test Document")
        doc.edit("Original content")
        doc.update_metadata("tags", ["important", "draft"])

        memento = doc.create_memento()

        # Próba modyfikacji przez getter nie powinna wpłynąć na oryginał
        retrieved_metadata = memento.get_metadata()
        retrieved_metadata["tags"].append("modified")
        retrieved_metadata["new_field"] = "new_value"

        # Pobierz ponownie - powinno być bez zmian
        fresh_metadata = memento.get_metadata()
        assert "modified" not in fresh_metadata["tags"]
        assert "new_field" not in fresh_metadata


class TestDemonstrateWorkflowSnapshots:
    """Testy demonstracji workflow snapshots (jeśli zaimplementowane)"""

    @pytest.mark.skip(reason="Optional feature - implement if you have time")
    def test_demonstrate_workflow_snapshots(self):
        """Test demonstracji workflow snapshots"""
        results = demonstrate_workflow_snapshots()

        assert isinstance(results, dict)
        assert "snapshots_created" in results
        assert "restore_operations" in results
        assert "milestone_usage" in results


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
