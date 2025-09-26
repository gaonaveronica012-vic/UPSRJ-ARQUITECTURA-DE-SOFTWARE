# entity_server.py
"""
This file exists so that tests can import entity_server.py
It simply imports the actual service from service/entity_service.py
"""

from exercises.basic_concepts.service.entity_service import EntityService

# Optional: instantiate a default service if needed by tests
# from exercises.basic_concepts.repository.interface import EntityRepository
# default_service = EntityService(repository=EntityRepository())
