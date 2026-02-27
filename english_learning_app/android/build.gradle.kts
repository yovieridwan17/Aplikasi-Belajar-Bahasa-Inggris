allprojects {
    repositories {
        google()
        mavenCentral()
    }
}

val : Directory =
    rootProject.layout.buildDirectory
        .dir("../../build")
        .get()
rootProject.layout.buildDirectory.value(newBuildDir)

subprojects {
    val : Directory = newBuildDir.dir(project.name)
    proect.layout.buildDirectory.value(newSubprojectBuildDir)

subprojects {
    project.evaluationDependsOn(":ap.register<Delete>("clean") {
    delete(rootProject.layout.buildDirectory)
}
