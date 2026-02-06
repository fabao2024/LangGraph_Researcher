# Copyright (c) 2026 Fabio Pettian. All rights reserved.
# Licensed under the MIT License.

from adk.skills import (
    format_commit_message, 
    add_license_header, 
    generate_pydantic_model, 
    validate_schema
)
import os

def test_git():
    print("Testing Git Skill...")
    msg = format_commit_message.invoke({
        "type": "feat", 
        "scope": "auth", 
        "subject": "add login endpoint", 
        "body": "Implements JWT auth."
    })
    print(f"Result: {msg}")
    assert "feat(auth): add login endpoint" in msg

def test_compliance():
    print("\nTesting Compliance Skill...")
    # Create dummy file
    with open("dummy.py", "w") as f:
        f.write("print('hello')")
    
    res = add_license_header.invoke({"file_path": os.path.abspath("dummy.py")})
    print(f"Result: {res}")
    
    with open("dummy.py", "r") as f:
        content = f.read()
    assert "Copyright (c) 2026" in content
    
    # Cleanup
    os.remove("dummy.py")

def test_codegen():
    print("\nTesting Codegen Skill...")
    json_input = '{"user": "fabio", "age": 30}'
    code = generate_pydantic_model.invoke({"json_input": json_input, "model_name": "User"})
    print(f"Result (snippet): {code[:50]}...")
    assert "class User(BaseModel):" in code

def test_data():
    print("\nTesting Data Skill...")
    schema = {
        "table": "users",
        "columns": [
            {"name": "id", "type": "int", "primary_key": True},
            {"name": "userName", "type": "text"} # snake_case violation
        ]
    }
    res = validate_schema.invoke({"schema_definition": schema})
    print(f"Result: {res}")
    assert "should be snake_case" in res

def test_git_invalid_type():
    print("\nTesting Git Skill (negative - invalid type)...")
    msg = format_commit_message.invoke({
        "type": "invalid",
        "scope": "auth",
        "subject": "test"
    })
    print(f"Result: {msg}")
    assert "invalid(auth): test" in msg

def test_compliance_nonexistent_file():
    print("\nTesting Compliance Skill (negative - nonexistent file)...")
    res = add_license_header.invoke({"file_path": "/nonexistent/file.py"})
    print(f"Result: {res}")
    assert "Error" in res or "not found" in res

def test_codegen_invalid_json():
    print("\nTesting Codegen Skill (negative - invalid JSON)...")
    code = generate_pydantic_model.invoke({
        "json_input": "{invalid json",
        "model_name": "Test"
    })
    print(f"Result: {code}")
    assert "Error" in code or "Invalid JSON" in code

def test_data_empty_schema():
    print("\nTesting Data Skill (negative - empty schema)...")
    schema = {
        "table": "empty_table",
        "columns": []
    }
    res = validate_schema.invoke({"schema_definition": schema})
    print(f"Result: {res}")
    assert "missing a Primary Key" in res or "failed" in res

if __name__ == "__main__":
    try:
        test_git()
        test_compliance()
        test_codegen()
        test_data()
        test_git_invalid_type()
        test_compliance_nonexistent_file()
        test_codegen_invalid_json()
        test_data_empty_schema()
        print("\nAll tests passed!")
    except Exception as e:
        print(f"\nTests failed: {e}")
