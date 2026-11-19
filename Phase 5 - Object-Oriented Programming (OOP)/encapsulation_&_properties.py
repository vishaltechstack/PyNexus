# ==============================================================================
# FILE: 17_encapsulation_and_properties.py
# TOPIC: Encapsulation, Name Mangling, and Pythonic @property Getters/Setters
# ==============================================================================

class DatabaseConfig:
    """
    Demonstrates Python's access conventions and validated properties.
    Python relies on naming conventions rather than strict 'private' keywords:
      - name    : Public (accessible everywhere)
      - _name   : Protected by convention (internal use; subclasses may access)
      - __name  : Private via name mangling (rewritten to _ClassName__name)
    """

    def __init__(self, host: str, port: int, password: str):
        self.host = host                        # Public attribute
        self._port = port                       # Protected attribute
        self.__password = password              # Private (name-mangled) attribute

    # 1. @property (GETTER)
    # Allows reading a computed or protected value like a normal attribute (obj.port)
    # instead of calling a Java-style getter method (obj.get_port()).
    @property
    def port(self) -> int:
        return self._port

    # 2. @<name>.setter (SETTER WITH VALIDATION)
    # Runs automatically whenever someone assigns to 'obj.port = value'.
    @port.setter
    def port(self, new_port: int) -> None:
        if not (1 <= new_port <= 65535):
            raise ValueError(f"Invalid port {new_port}: must be between 1 and 65535.")
        self._port = new_port

    # 3. READ-ONLY PROPERTY (No setter defined)
    @property
    def connection_uri(self) -> str:
        return f"mysql://{self.host}:{self._port}/app_db"

    def mask_password(self) -> str:
        return "*" * len(self.__password)


# --- Testing Encapsulation & Validation ---
db = DatabaseConfig("127.0.0.1", 3306, "SuperSecret@2026")

print("Initial URI:", db.connection_uri)        # Calls @property seamlessly
db.port = 3307                                  # Calls @port.setter seamlessly
print("Updated URI:", db.connection_uri)
print("Masked Password:", db.mask_password())

# Attempting invalid port triggers setter validation:
try:
    db.port = 99999
except ValueError as err:
    print(f"[Validation Blocked] {err}")

# Direct access to db.__password raises AttributeError due to name mangling:
try:
    print(db.__password)
except AttributeError as err:
    print(f"[Access Restricted] {err}")
