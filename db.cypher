// Constraints

CREATE CONSTRAINT FOR (n:Node) REQUIRE n.id IS UNIQUE; // Example

// Indexes

CREATE INDEX has_child_field1_field2_index FOR ()-[r:HAS_CHILD]-() ON (r.field1, r.field2); // Example
