
        .dir("../../build")
        .get()
rootProject.layout.buildDirectory.value(newBuildDir)

subprojects {
    val : Directory = newBuildDir.dir(project.name)
    proect.layout.buildDirectory.value(newSubprojectBuildDir)

subprojects {
    project.evaluationDependsOn(":ap.register<Delete>("clean")