def test_register_plugin():
    # Arrange
    plugin = MockPlugin()
    api = PluginAPI()
    
    # Act
    api.register_plugin(plugin)
    
    # Assert
    assert plugin in api.plugins

def test_unregister_plugin():
    # Arrange
    plugin = MockPlugin()
    api = PluginAPI()
    api.register_plugin(plugin)
    
    # Act
    api.unregister_plugin(plugin)
    
    # Assert
    assert plugin not in api.plugins

def test_handle_idespecific_error():
    # Arrange
    api = PluginAPI()
    
    # Act
    result = api.handle_error("IDE_Specific_Error")
    
    # Assert
    assert result == "Handled IDE_Specific_Error gracefully"